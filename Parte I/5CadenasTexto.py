#Cadenas de texto

"""Cd = "Este es un \"ejemplo\" de cadenas \npara dar salto de linea \ttabulacion \f\v"
print(Cd)"""

#Cadenas aritmeticas

"""Cd1 = "Contetonacion"
Cd2 = " de cadenas"

print(Cd1 + Cd2)
print(Cd2 * 2)

Nombre = "David"
print("Hola usuario: "+ Nombre)"""

#Debanado de cadenas

"""Cd = "Ejemplo de debanado de cadena"

print(len(Cd))
print(Cd[3])
print(Cd[0 : 10])
print(Cd[ : 20])
print(Cd[20 : ])
print(Cd[-2 : ])"""

#Metodos

"""Cd = "Estoy utilizando los metodos de Python"

print(Cd.lower()) #Transforma mayusculas en minusculas
print(Cd.upper()) #Transforma minusculas a mayusculas
print(Cd.capitalize()) #Muestra solo la primera en mayuscula
print(Cd.title()) #Cada plabara en mayuscula la primera
print(Cd.swapcase()) #Invierte mayusculas y minusculas"""

#Ejercicio 1

Cd = "Te quiero solo como amigo"

print(len(Cd))
print(Cd[0 : 2])
print(Cd[-3 : ])
print(Cd[0 : 25 : 2])
print(Cd[: :-1])
print(Cd+Cd[: :-1])


#Ejercicio 2

Cd1 = "eparado"

print(Cd1)
Cd2 = Cd1.replace("",",")
print("S",Cd2)