import base64
import io
import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "certificate_template.svg"
OUTPUT_SVG_PATH = BASE_DIR / "certificado_generado.svg"
OUTPUT_PNG_PATH = BASE_DIR / "certificado.png"

name = " ".join(sys.argv[1:]).strip() or "Nombre del participante"

template = TEMPLATE_PATH.read_text(encoding="utf-8")

if "%s" not in template:
    raise ValueError("No se encontró el marcador de nombre en la plantilla SVG.")

updated_template = template.replace("%s", name, 1).replace("%dpx", "56px", 1)
OUTPUT_SVG_PATH.write_text(updated_template, encoding="utf-8")

match = re.search(r'href="data:image/(?P<ext>png|jpeg|jpg);base64,(?P<data>[A-Za-z0-9+/=]+)"', updated_template)
if not match:
    raise ValueError("No se encontró una imagen base64 en la plantilla SVG.")

image_bytes = base64.b64decode(match.group("data"))
image = Image.open(io.BytesIO(image_bytes)).convert("RGBA")

text_match = re.search(r'<text id="participant-name"[^>]*x="(?P<x>\d+)"\s+y="(?P<y>\d+)"', updated_template)
if not text_match:
    raise ValueError("No se encontró la posición del texto del nombre en la plantilla SVG.")

x = int(text_match.group("x"))
y = int(text_match.group("y"))

font_size = 56
font = None
for font_path in [
    "C:/Windows/Fonts/arial.ttf",
    "C:/Windows/Fonts/times.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]:
    if os.path.exists(font_path):
        font = ImageFont.truetype(font_path, font_size)
        break

if font is None:
    font = ImageFont.load_default()

canvas = Image.new("RGBA", image.size, (255, 255, 255, 0))
canvas.paste(image, (0, 0))

draw = ImageDraw.Draw(canvas)
text_bbox = draw.textbbox((0, 0), name, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = x - text_width / 2
text_y = y - text_height / 2

draw.text((text_x, text_y), name, fill=(0, 0, 0, 255), font=font)
canvas.save(OUTPUT_PNG_PATH)

# print(f"Certificado exportado como PNG: {OUTPUT_PNG_PATH}")
print(f"Hola {name}, adjuntamos el certificado de aprobación de nuestro curso de análisis de datos en Python.\nAgradecemos tu participación, y te esperamos en futuros cursos.\nSaludos cordiales.")

