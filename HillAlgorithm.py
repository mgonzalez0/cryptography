import numpy
import numpy as np
def obtenerKeyMatrix():
    row = int(input("Ingrese el grado de la matriz:"))
    column = row
    # Initialize matrix
    matrixKey = []
    print("Ingrese los datos en una sola fila")
    for i in range(row):
        a = []
        for j in range(column):
            a.append(int(input()))
        matrixKey.append(a)

    for i in range(row):
        for j in range(column):
            print(matrixKey[i][j], end=" ")
        print()
    return matrixKey

def gcd(a,b):
    cociente = 0
    if a > b:
        cociente = int(a / b)
        residuo = a%b
        print("Cociente: %f" %cociente)
        print("Residuo: %f" % residuo)
        if residuo != 0:
            a = b
            b = residuo
            gcd(a,b)
        else:
            print("El GCD es: %d" %b)
    else:
        print("a no puede ser mayor que b")

#Establecemos el valor de cada letra
llaves = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7,'i': 8,'j': 9,'k': 10,'l': 11,'m': 12,'n': 13,'o': 14,'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,'u': 20,'v': 21,'w': 22,'x': 23,'y': 24,'z': 25}
llavesInv = {v: k for k, v in llaves.items()}
textoPlano = input("Ingrese el texto a cifrar: ")
textoLlaves = {}
textoCharAt = list(textoPlano)
codigoPlano = []
indice = 1
matrizPlano = []
cipherText = []
a= []
for caracter in textoCharAt:
    codigoPlano.append(llaves[caracter])
    textoLlaves[caracter] = llaves[caracter]
    a.append(llaves[caracter])
    if indice % 3 == 0:
        matrizPlano.append(a)
        a = []
    indice += 1
if len(a) > 0:
    matrizPlano.append(a)
print("El texto convertido a numeros es: ")
for caracter in codigoPlano:
    print(caracter, end=' ')
print()
for key in textoLlaves:
    print("%s  ---> %d" %(key, textoLlaves[key]), end=' ')
print()
print("-------------  MATRIZ QUE CONTIENE LLAVE ------------")
matrixArray = numpy.asarray(obtenerKeyMatrix())
print("-----------------------------------------------------")
print("----------------TEXTO CIFRADO -----------------")
for slot in matrizPlano:
    slotArray = numpy.array(slot)
    cipherText.append(list(np.matmul(slotArray,matrixArray)))
print(cipherText)
print("-----------------------------------------------------")
print("--------------- CON MODULO 26 ------------------")
cipherText26 = []
for slot in cipherText:
    a = []
    for element in slot:
        a.append(element%26)
    cipherText26.append(a)
print(cipherText26)
cipherTextString = []
for slot in cipherText26:
    for element in slot:
        cipherTextString.append(llavesInv[element])
print("--------------- TEXTO CIFRADO -------------")
print("".join(cipherTextString).upper())

