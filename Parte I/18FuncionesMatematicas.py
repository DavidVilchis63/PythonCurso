#Funciones matematicas 
"""
import math
import random

print(math.pow(10,3)) #Eleva numeros al valor asignado

print(math.sqrt(64)) #Calcula raiz cuadrada
print(math.isqrt(64)) #Resultado entero

print(math.sin(90)) #Calculo de seno, etc
print(math.cos(90))
print(math.tan(90))

print(math.factorial(5)) #Sacar factoriales

print(random.randint(0,100)) #Toma un numero al azar del rango indicado

#Nota: Para usar el valor return en funciones es necesario usar
#      un print para que el valor se vea
"""

#Ejercicio 1
"""
def pedirValores():
    num1 = float(input("Ingrese numero 1: "))
    num2 = float(input("Ingrese numero 2: "))

    if num1 > num2:
        return 1

    elif num1 < num2:
        return -1

    else:
        return 0

print(pedirValores())
"""

#Ejercicio 2

def calculoTotal():
    cantidad = float(input("Ingrese el monto que esta pagando: "))
    iva = int(input("Ingrese el valro del IVA: "))

    if iva != 0:
        if iva > 0:
            montoTotal = (cantidad * (iva / 100)) + cantidad
            return montoTotal
        else:
            print("Valor no aceptado para el IVA")
    else:
        montoTotal = (cantidad *0.21) + cantidad
        return montoTotal

print("El total a pagar es: ", calculoTotal())
