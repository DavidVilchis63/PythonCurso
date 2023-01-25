#Parametros y argumentos
"""
def suma(num1,num2): #num son los parametros
    resultado = num1 + num2
    return resultado

print(suma(10,10)) #Aqui van los argumentos, el valor que tomara cada variable (Parametros)
"""

#Variables globales
"""
def valores():
    global var1  #global sirve para hacer una variable global
    global var2

    var1 = 110
    var2 = 40
    resultado = var1 + var2
    return resultado

print(valores())

resta = var1 - var2
print(resta)
"""

#Valores indefinidos
"""
def argumento(*num): #Al usar * los elementos ingresados se almacenan en una tupla
    return type(num)

print(argumento(10,9,0))
"""

#Ejercicio 1

def areaRectangulo(base, altura):
    total = base * altura
    return total

print(areaRectangulo(10,5))

def areaCirculo (radio):
    import math

    total = math.pi*(math.pow(radio,2))
    return total

print(areaCirculo(10))

#Ejercicio 2

def muestra(*valores):
    return len(valores)

print(muestra(10,3,4,5))