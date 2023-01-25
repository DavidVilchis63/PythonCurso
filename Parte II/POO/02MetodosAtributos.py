#Metodos y atributos

class FabricaTelefonos(): #Clase
    marca = "MarcaTelefono" #Atributos
    color = "Azul"
    memoriaRAM = 32
    almacenamiento = 128

    #Metodo de instancia (Porque es un metodo creado, no por defecto)
    def llamar(self, mensaje): #Metodo ya que esta dentro de una clase (Alguna funcion que puede hacer el objeto)
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando musica")

telefono = FabricaTelefonos() #Objeto
telefono.marca #De esta manera se le atrituye el atributo de la clase al objeto
telefono.color
telefono.memoriaRAM
telefono.almacenamiento
print(telefono.color)

print(telefono.llamar("Cadena de mensaje"))

telefono.escucharMusica()
