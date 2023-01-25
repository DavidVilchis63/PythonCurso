#Funcion de self
"""
class FabricaTelefonos(): #Clase
    marca = "MarcaTelefono" #Atributos
    color = "Azul"
    memoriaRAM = 32
    almacenamiento = 128

    def elaborarOtroTelefono(self): #Sirve para englobar un atributo a otda una clase
        self.marca = "OtraMarca"

telefono = FabricaTelefonos()
print(telefono.marca) 

telefono.elaborarOtroTelefono()
print(telefono.marca) """

#Metodo init

class FabricaTelefono():
    def __init__(self, marca, color): #Metodo constructor, se ejecuta al inicar el objeto
        self.marca = marca
        self.color = color

telefono = FabricaTelefono("MarcaTelefono", "Verde")
print(telefono.marca)
print(telefono.color)