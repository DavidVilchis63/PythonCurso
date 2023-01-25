#Encapsulamiento
#Es un atributo que no se puede acceder por fuera, solo desde la misma clase
""" 
class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador
    
class B():
    def __init__(self):
        self.__contador = 0

    def incrementar(self):
        self.__contador += 1
    
    def cuenta(self):
        return self.__contador

print("Objeto 1")
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())

print("Objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
#print(b.__contador) 
#Intenta acceder por fuera por eso manda error
 """

#Profundizar en encapsulamiento

class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0

    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

a = A()
# print(a.cuenta) #Si las variables tienen _ no deben ser llamadas las variables de esta manera
# a.cuenta = 20
# print(a.cuenta)