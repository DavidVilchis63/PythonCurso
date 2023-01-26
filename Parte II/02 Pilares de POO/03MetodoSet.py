#Trabajar con metodo set para cambiar valores

class A():
    def __init__(self):
        self._cuenta = 0 #Al poner _ es un atributo encapsulado
        self._contador = 0

    @property #Palabra reservada para que se reconozca como atributo un metodo
    def cuenta(self): #Metodo de instancia para llamar al valor de una variable
        return self._cuenta

    @cuenta.setter #Palabra reservada para modificar un atributo (Metodo Set)
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    @property
    def contador(self):
        return self._contador

    @contador.setter
    def contador(self, contador):
        self._contador = contador


a = A()
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
print(a.contador)
a.contador = 10
print(a.contador)