#Metodos especiales

class FabricaTelefonos(): #Clase
    def __init__(self, marca): #Metodo construtor
        self.marca = marca
        print("El objeto {} ha sido creado".format(self.marca))

    def __str__(self):
        return "El objeto es {}".format(self.marca)        
        
    def __del__(self): #Al finalizar elimina todo
        print("El objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefonos("Nokia")
print(telefono.marca)
print(telefono)
        