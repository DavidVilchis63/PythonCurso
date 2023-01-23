#Funciones propias de Python
"""
num = "70"
lista = [12,60,30,-4,50]

print(type(num))
print(type(int(num)))
print(type(float(num)))

print(len(lista))
print(max(lista))
print(min(lista))
"""

#Crear funciones propias
""" 
def pruebaFuncion():
    print("Hola mundo")

#pruebaFuncion()

def tabla7():
    for i in range(11):
        print("7 x {} = {} ".format(i, i*7))

tabla7() """

#Ejercicio 1

listaIncial = []

def agregarElementos():
    nuevoValor = int(input("Ingrese un numero nuevo: "))
    listaIncial.append(nuevoValor)

i = 0

while i < 10:
    agregarElementos()
    i = i + 1   

print(listaIncial)

listaPares = []
listaImpares = []

def separarNumeros():
    for numero in listaIncial:
        if numero % 2 == 0:
            listaPares.append(numero)
        else:
            listaImpares.append(numero)

separarNumeros()
print("La lista de numeros pares es: ", listaPares)
print("La lista de numeros impares es: ",listaImpares)