#Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self._nombre, self._nota))

    def resultados(self):
        if self._nota < 6:
            print("Nota reprobatoria")
        else:
            print("Nota aprobatoria")

    @property 
    def nombre(self): 
        return self._nombre

    @nombre.setter 
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota


estudiante1 = Estudiante("David", 5)
#print(estudiante1.nombre)
#print(estudiante1.nota)
estudiante1.imprimir()
estudiante1.resultados()

estudiante1.nombre = "Maggie"
estudiante1.nota = 8
#print(estudiante1.nombre)
#print(estudiante1.nota)
estudiante1.imprimir()
estudiante1.resultados()