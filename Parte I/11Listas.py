#Ejemplo de listas:
#Los datos se pueden cambiar

#EjemploLista = ["pan", 5, 30, "cadena"]
#Posicion         0    1   2      3

"""
#Introduccion listas

lista1 = ['Python', 120, "Nombre", 4.14, 6.28]

print(type(lista1))
print(lista1)
print(lista1[3]) #Los corchetes mandan llamar al elemento indicado
print(len(lista1)) #Cantidad de elementos en la lista

#cambiar valores de la lista
lista1[0] = "OtroValor" #Corchetes seleccionan el elemento a cambiar
print(lista1)

"""
#Trabajando listas (Devanado)
"""
lista2 = [10, 20, 3.14, "Walter", "Coto", 7, "Estudiante", "Cuaderno"]

print(lista2[0 : 5]) #Imprime hasta la posicion 5 pero no el 5, ese es el limite 
print(lista2[ : 2]) #Imprime desde la posicion 0 hasta la 2, pero no el 2
print(lista2[1 : ]) #Imprime desde la posicion 1 hasta el limite de la lista
print(lista2[-1]) #Empieza del final de la lista, pero aqui la ultima posicion si es la -1 y no 0
print(lista2[-5 : -2]) #Otra forma de devanado empezando desde el final
"""

#Metodos de listas
"""
lista3 =[1, 2, 3, 4, 5]
print(lista3)

#Agregar valores con metodo append (Se agrega al final de la lista)
lista3.append(5) 
print(lista3)
lista3.append("Python")
print(lista3)

#Agregar datos con metodo insert (Se agrega en una posicion indicada) (posicion, valor)
lista3.insert(2, 2.5)
print(lista3)

#Cuenta cantidades de veces que hay un elemento en una lista
print(lista3.count(5))

#Metodo para buscar datos, retorna la primera posicion donde se encuentre el elemento
print(lista3.index("Python"))

#Metodo para ordenar lista de manera ascendente(sort) y descendente(reverse)
lista3a = [5, 3, 1, 4, 2]
print(lista3a)
lista3a.sort()
print(lista3a)
lista3a.reverse()
print(lista3a)

#Modificar datos ya ingresados
lista3b = ["Python", 24, "Rene", "alexander", 12]
print(lista3b)
lista3b[3] = "Alexander"
print(lista3b)

#Metodo para eliminar datos de una lista, elimina el ultimo valor(pop), con remove elimina el valor ingresado
lista3b.pop()
print(lista3b)
lista3b.remove("Python")
print(lista3b)
"""

#Operadores con las listas
"""
lista4 = [1, 2, 3]
lista5 = [4, 5, 6]

lista6 = lista4 + lista5 #Solo se puede sumar listas, y no se pueden contatenar con +
print(lista6)
print("Esto es una lista: ", lista6)

#Llenar listas
lista7 = []

edad = int(input("Ingrese tu edad: "))
lista7.append(edad)
print(lista7)
"""

#Ejercicio 1
"""
listaEjercicio = [20, 50, "Curso", "Python", 3.14]

print(listaEjercicio)
dato1 = input("Ingrese dato 1 a sustiruir: ")
dato2 = input("Ingrese dato 2 a sustiruir: ")

listaEjercicio[0] = dato1
listaEjercicio[1] = dato2

print(listaEjercicio)
"""

#Ejercio 2

listaEjercicio2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(listaEjercicio2)
listaEjercicio2[4] = listaEjercicio2[4] * 2
listaEjercicio2[7] = listaEjercicio2[7] * 2
listaEjercicio2[9] = listaEjercicio2[9] * 2
print(listaEjercicio2)