#Trabajar con metodo get para conocer valores en las clases

class A():
    def __init__(self):
        self._cuenta = 0 #Al poner _ es un atributo encapsulado
        self._contador = 2

    @property #Palabra reservada para que se reconozca como atributo un metodo
    def cuenta(self): #Metodo de instancia para llamar al valor de una variable
        return self._cuenta

    @property
    def contador(self):
        return self._contador


a = A()
print(a.cuenta)
print(a.contador)
