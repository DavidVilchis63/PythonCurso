#Que es la herencia

class Animales(): #Clase padre
    def habla(self): #Metodo
        print("Texto de ejemplo")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal))

#Clases hijas
class Perro(Animales): #De esta manera todos los metodos, y atributos pasan a esta clase
    pass #Forma de indicar que se dejara en blanco

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal 

animal = Animales()
animal.habla()

manchas = Perro()
manchas.habla()

abeja = Abeja("Abeja")
abeja.descripcion()