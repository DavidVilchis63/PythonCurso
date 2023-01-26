#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self):
        self._dato1 = int(input("Ingrese el numero 1: "))
        self._dato2 = int(input("Ingrese el numero 2: "))

    @property
    def dato1(self):
        return self._dato1
    
    @dato1.setter
    def dato1(self, dato1):
        self._dato1 = dato1
    
    @property
    def dato2(self):
        return self._dato2

    @dato2.setter
    def dato2(self, dato2):
        self._dato2 = dato2

    def suma(self):
        self.resultadoSuma = self.dato1 + self.dato2
        print("El resultado de la Suma es: ", self.resultadoSuma)

    def resta(self):
        self.resultadoResta = self.dato1 - self.dato2
        print("El resultado de la resta es: ", self.resultadoResta)
    
    def multiplicacion(self):
        self.resultadoMulti = self.dato1 * self.dato2
        print("El resultado de la multiplicacion es: ", self.resultadoMulti)

    def division(self):
        self.resultadoDivision = self.dato1 / self.dato2
        print("El resultado de la division es: ", self.resultadoDivision)
    
    

primerConjunto = Calculadora()
primerConjunto.suma()
primerConjunto.resta()
primerConjunto.multiplicacion()
primerConjunto.division()

