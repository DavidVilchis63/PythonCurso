#Ejemplos de while

""" i = 1 

while i <= 10:
    print("Ejemplo de iterador: {} Salto".format(i))
    i += 1 
"""

#Ejercicio1
"""
numero = int(input("Ingrese un numero para obtener su tabla de multiplicar:"))

i = 1
n = 1

print("Tabla del: ", numero)

while i <= 10:
        
    multiplicacion = i*numero
    print(" {} x {} = {}".format(numero,n,multiplicacion))
    n = n + 1
    i = i + 1
"""

#Ejercicio2

edad = int(input("Escriba su edad: "))
i = edad

while i > 0:
    print("Ya cumpliste: ", edad)
    edad = edad - 1
    i = i - 1
