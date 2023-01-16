#Bucles For
"""
lista = ["Uno", "Dos", "Tres"]
tupla = (1,2,3,4,5)

for i in lista:
    print(i)

for j in tupla:
    print(j)

#Para recorrer rangos

for k in range(0, 10, 3): #Si ocupamos numeros negativos recordar el menor primero, ejemplo -10 es menor que-1
    print(k)


#Funcion continue and break para detener una iteraccion o saltar

for i in range(1, 11):
    print(i)
    if i == 5:
        break

for j in range(1,11):
    if j == 8:
        continue
    print(j)

"""

#Ejercicio 1
"""
for i in range(1, 11):
    print(i)

num1 = int(input("Selecciona un numero: "))
num2 = int(input("Selecciona un segundo numero: "))

if num1 < num2:
    print("El rango de tus  numeros es:")
    for i in range(num1, num2+1):
        print(i)

else:
    for i in range(num2, num1+1):
        print(i)

#Ejercicio 2
"""
num3 = int(input("Selecciona un numero: "))
num4 = int(input("Selecciona un segundo numero: "))

for j in range(num3, num4+1):
    if j % 2 ==0:
        continue
    print(j)