#Revision de init

class FabricaTelefonos():

    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Nokia", "Negro", "Azul", "Rojo", M1 = 500, M2 = 700)
print(telefono.marca)
print(telefono.colores) #Tupla
print(telefono.modelos) #Diccionario

telefono.memoria = 512 #Crea atributos temporales
print(telefono.memoria)