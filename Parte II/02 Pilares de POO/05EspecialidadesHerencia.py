#Posibles errores al trabjar con herencia

class Animales():
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre) #Hereda init demanera correcta
        self.sonido = sonido

perro = Perro("Manchas", "Ladrido")
print(perro.nombre)
print(perro.sonido)