#Diccionarios
#Las claves no se pueden repetir
"""

diccionario = {"Ususario": "Wcoto", "Contrasenia": 12345}
print(diccionario)
print(type(diccionario))

diccionario1 = {"Nombre" : "Walter", "Apellido" : "Coto", "Estatura": 1.80}
print(diccionario1.keys())
print(diccionario1.values())
print(diccionario1["Estatura"]) #De esta forma manda a llamar una clave especifica dentro del diccionario

#Agregar valores al diccionario

diccionario1["Peso"] = "58 kg"
print(diccionario1)

#Modificar un valor existente

diccionario1["Nombre"] = "OtroValor"
print(diccionario1)
"""

#Metodos de diccionarios
#Eliminar elementos del diccionario
"""
diccionario2 = {1: 2, 2: 3, 3: 4}
print(diccionario2)
diccionario2.pop(3)
print(diccionario2)

#diccionario2.clear()
print(diccionario2) #Limpia todos los elementos que esten en el diccionario

#Obtener un valor con el metodo get
print(diccionario2.get(2)) #Trae el valor de la llave que se ingrese

#Recibe un valor de llave y lo agrega
diccionario2.setdefault(3, 5)
print(diccionario2)

#Combinar valores de dos diccionarios
diccionario3 ={4: 5, 6: 7}

diccionario2.update(diccionario3)
print(diccionario2)

#Copiar diccionario
diccionario2.copy()
print(diccionario2)
"""

#Ejercicio 1