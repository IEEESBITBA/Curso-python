## NO DIFUNDIR A LOS PARTICIPANTES

## SOLUCIONARIO CLASE 1
# Funciones
#Solucion al ejercicio borrar antes de la clase
def usCont(u,c):
    if (u=="Juan" and c=="12345_") or (u=="Pablo" and c=="xDcFvGbHn"):
        print("Login OK")
    else:
        print("Login NOK")
   
usCont("Pablo","xDcFvGbHn")
usCont("Juan","12345_")
usCont("Juan","xDcFvGbHn")
#end

# Entrevista Ingematica
def printNum(n):
  s=""
  if n%3==0:
    s = "N3"
  if n%5==0:
    s = s+"N5"
  if s=="":
    print(n)
  else:
    print(s)

for x in range(1,101):
  printNum(x)
#end
  
## SOLUCIONARIO CLASE 2

#Naranjas de Miguel
P="011"  
def leerPedido(pedido):
  naranjas=0
  bananas=0
  for i in range(0,len(pedido)): 
    letra = pedido[i]
    if letra=="0": 
      naranjas+=1 
    else:
      bananas+=1
  return naranjas,bananas

def cuantasDar(naranjas,bananas):
  naranjasParaHermana = 0
  bananasParaHermana = 0
  if naranjas<2:
    naranjasParaHermana = 0
  else:
    naranjasParaHermana = 1 
  if bananas > 1:
    bananasParaHermana = 2
  else:
    bananasParaHermana = bananas
  return naranjasParaHermana,bananasParaHermana

n,b = leerPedido(P) #Leo pedido y guardo a memoria las frutas que tengo
nh,bh = cuantasDar(n,b) #Aqui calculo naranjas para darle a la hermana

print("Bienvenido Miguel. Hoy Dar ",nh," Naranja y ",bh," banana(s).")
#end

#Menu y opciones
espanolToChaos = {"ve":"regards","bien":"bom","se":"it"}
oracion = "se ve bien!"
whitespace = [" ",".",",","!","?"]

resultado = ""
palabra = ""
for i in range(0,len(oracion)):
  letra=oracion[i]
  if letra in whitespace:
    if palabra!="":
      resultado = resultado+espanolToChaos[palabra]
    
    resultado = resultado+letra
    palabra=""
  else:
    palabra = palabra+letra
print(resultado)
#end

#Dr. Chaos
espanolToChaos = {"ve":"regards","bien":"bom","se":"it"}
oracion = "se ve bien!"
whitespace = [" ",".",",","!","?"]

resultado = ""
palabra = ""
for i in range(0,len(oracion)):
  letra=oracion[i]
  if letra in whitespace:
    if palabra!="":
      resultado = resultado+espanolToChaos[palabra]
    
    resultado = resultado+letra
    palabra=""
  else:
    palabra = palabra+letra
print(resultado)
#end

# Call me diff for short
x = [-2,-1,0,1,2,3,4,5,6,7]
e = (1+1/999999)**999999
exp = [e**x for x in range(10)]

def diff(v):
  der= [0]*(len(v)-1)#Primer paso. Crear la lista 
  for i in range(len(der)):
    der[i]=v[i+1]-v[i]
  return der
# OTRA FORMA mas en linea con la matematica anunciada antemano. Se podria explicar un poco en clase
def diff2(X):
  n=len(X)
  der = [0 for i in range(n-1)]
  for i in range(n-1):
    der[i]=X[i+1]-X[i]
  return der
print(diff2(x))
print(diff(exp))
print(exp)# Lo ideal es que la derivada hubiera sido la misma pero toma derivada en el punto medio entre los dos numeros de la list jajaja
#end

# TRUCO
# solución propuesta (Ariel)
valorCarta = dict()
valorCarta["1 de espada"] = 14 # Mucho special cases
valorCarta["1 de basto"] = 13
valorCarta["7 de espada"] = 12
valorCarta["7 de oro"] = 11
valor = 10
for x in [3,2,1,12,11,10,7,6,5,4]: # Requiere crear un iterable no lineal(discontinuo en verdad)
    if x == 1:
        palos = ["oro","copa"]
    elif x == 7:
        palos = ["basto", "copa"]
    else:
        palos = ["oro","copa","basto","espada"]
    
    for palo in palos:
        valorCarta[str(x)+" de " + palo] = valor
    
    valor -= 1

def dueloDeCartas(cartaA, cartaB):
    if valorCarta[cartaA] > valorCarta[cartaB]:
        return cartaA
    elif valorCarta[cartaA] < valorCarta[cartaB]:
        return cartaB
    else:
        return "empate"
print(dueloDeCartas("7 de basto","1 de basto")) #encontre más errores! el 7 trae problems!
print(dueloDeCartas("1 de copa", "1 de oro"))
print(dueloDeCartas("7 de copa","3 de copa"))
print(valorCarta) 

#end

