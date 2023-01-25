#Try
"""
while True:
    try: 
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
        break
    except:
        print("Valor no valido para edad")
    finally:
        print("La ejecucion ha finalizado")
"""

#Excepciones multiples

while True:
    try:
        num1 = int(input("Ingrese un numero: "))
        resultado = 100 / num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

while True:
    try: 
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
        break
    except ValueError:
        print("Valor no valido para edad")

while True:
    try: 
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
        break
    except KeyboardInterrupt:
        print("\nCancelaste la ejecucion")
        break


