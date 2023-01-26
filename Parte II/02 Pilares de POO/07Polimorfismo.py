#Polimorfismo, modificar metodos heredados de un metodo padre

class Animales(): 
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self): #Metodo
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Texto de ejemplo") 

class Pez(Animales):
    def hablar(self):
        print("Segundo texto de ejemplo")

perro = Perro("Mensaje del metodo init")
perro.hablar()

animal = Animales("Mensaje de metodo init 2")
animal.hablar()

pez = Pez("Mensaje de metodo init 3")
pez.hablar()