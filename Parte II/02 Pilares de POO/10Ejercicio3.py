#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    
class Carro(Fabrica):
    def caracteristicas(self):        
        print("Elejiste un carro de {} llantas \nColor: {} \nPrecio de: {}".format(self.llantas, self.color, self.precio))
    
class Moto(Fabrica):
    def caracteristicas(self):
        print("Elejiste un carro de {} llantas \nColor: {} \nPrecio de: {}".format(self.llantas, self.color, self.precio))

vehiculo2 = Carro(4, "Verde", 4000)
vehiculo3 = Moto(2, "Azul", 2000)

vehiculo2.caracteristicas()
vehiculo3.caracteristicas()