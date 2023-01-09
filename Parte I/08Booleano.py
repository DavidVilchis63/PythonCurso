#Booleanos

"""verdadero = True
falso = False

print(type(verdadero))
print(type(falso))"""

#Operadores relacionales
"""
num1 = 1000
num2 = 500
num3 = 1000
cadena = "Comparaciones de strings"
cadena1 = "Comparacion de strings"

print(num1 > num2)
print(num2 < num1)
print(num1 >= num3)
print(num1 == num2) #Igualación comparar si son iguales
print(num1 != num2) #Diferente de

print(cadena == cadena1)
"""
#Operadores Logicos (And, or, not)
"""
print(10 > 2 and 9 > 100) 
print(88 <= 45 or 60 > 110)
print(not 90 != 90)
"""

#Metodos booleanos

cadena = "Metodos booleanos para Strings"

print(cadena.startswith("M")) #Verifica si empieza con la letra entre parentesis
print(cadena.endswith("M")) #Verifica si empieza con la letra entre parentesis

cadena1 = "TODO MAYUSCULA"

print(cadena1.isupper())
print(cadena1.islower())