#Tuplas, estas no tienen muchos metodos ya que los valores no se pueden cambiar
"""
tupla = (1,2,3,4,5)

print(tupla)
print(type(tupla))

#Imprimir un valor con posiciones
print(tupla[2])

#Hacer devanados
print(tupla[0 : 3]) #No imprime la ultima posicion seleccionada

#Sumar tuplas
tupla1 = (6,7,8,9)
print(tupla + tupla1)
"""

#Ejercicio 1

tuplaMeses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

valor = int(input("ingrse un numero para conocer el mes: "))
valorNuevo = valor - 1

if valorNuevo < 12:
    print(tuplaMeses[valorNuevo])

else:
    print("Ingrese un valor menor a 12")

#Ejercicio 2

tuplaAlfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

valorLetra = int(input("ingrse un numero para conocer la letra: "))
valorNuevoLetra = valorLetra - 1

if valorNuevoLetra < 26:
    print(tuplaAlfabeto[valorNuevoLetra])

else:
    print("Ingrese un valor menor  a 27")