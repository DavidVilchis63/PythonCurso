#Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...". Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parametro

class Marino():
    def hablar(self):
        print("Hola....")

class Pulpo(Marino):
    def hablar(self):
        print("Soy un pulpo")

class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

animal0 = Marino()
animal0.hablar()

animal1 = Pulpo()
animal1.hablar()

animal2 = Foca()
animal2.hablar("Mensaje de ejemplo")