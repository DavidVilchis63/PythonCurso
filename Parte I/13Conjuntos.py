#Metodos de conjuntos

conjunto1 = {1,2,3,4,5}
lista = {1,2,2,4,4}

print(conjunto1)
print(lista)

#Añadir elementos a los conjuntos
conjunto1.add(20)
print(conjunto1)

#Eliminar elementos del conjunto, este elimina valores ingresados
conjunto1.remove(4) #.discard sirve igual
print(conjunto1)

conjunto1.pop()
print(conjunto1)

#Añade elementos iterables

conjunto1.update([1,2,3])
print(conjunto1)

#limpiar el conjunto
conjunto1.clear()
print(conjunto1)