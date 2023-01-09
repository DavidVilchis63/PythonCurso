# Condional if and else

"""
Edad = 17

if Edad >= 18:
    print("Eres mayor de edad")

else: 
    print("No eres mayor de edad")

"""

# Condicional Elif

"""
letra = "u"

if letra.lower() == "a":
    print("Esta vocal es A")

elif letra.lower() == "e":
    print("Esta vocal es E")

elif letra.lower() == "i":
    print("Esta vocal es I")

elif letra.lower() == "o":
    print("Esta vocal es O")

elif letra.lower() == "u":
    print("Esta vocal es U")

else:
    print("Error ingrese una vocal")

"""

# Condicionales anidados

"""
nombre = "Juan"
edad = 18

if nombre == "Juan":
    if edad >= 18:
        print("Eres Juan tienes mayoria de edad")
    else:
        print("Eres Juan pero no tienes mayoria de edad")
        
else:
    print("No eres Juan")

"""

# Ejercicio 1
"""
letra = input("Ingrese una letra: ")

if letra.lower() == "a":
    print("Es vocal")

elif letra.lower() == "e":
    print("Es vocal")

elif letra.lower() == "i":
    print("Es vocal")

elif letra.lower() == "o":
    print("Es vocal")

elif letra.lower() == "u":
    print("Es vocal")

else:
    print("No es vocal")
"""

# Ejercicio 2
"""
numero = int(input("Ingrese un numero: "))

if numero >= 0:
    print("El valor absoluto del numero es =", numero)

else:
    absoluto = (-1)*numero
    print("El valor absoluto del numero es =", absoluto)
"""

#Ejercicio 3

palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3: #len sirve para medir la cantidad de caracteres en una cadena 
    print("Las palabras no riman, tienen menos de 3 caracteres")

elif palabra1[-3:] == palabra2[-3:]: #negativo empiezo en 1, positivo en 0
    print("Las palabras riman, las ultimas tres letras son iguales")

elif palabra1[-2:] == palabra2[-2:]:
    print("Las palabras riman un poco, las ultimas dos letras son iguales")

else:
    print("Las palabras no riman")



#Ejercicio 4
"""
A = "Partido Rojo"
B = "Partido Verde"
C = "Partido Azul"

voto = input("Vote por el candidato que desee: ")

if voto.upper() == "A":

    print("Usted a votado por el ", A)

elif voto.upper() == "B":

    print("Usted a votado por el ", B)

elif voto.upper() == "C":

    print("Usted a votado por el ", C)

else:

    print("Opcion erronea, los candidatos son A, B, o C")

"""