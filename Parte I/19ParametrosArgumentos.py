#Parametros y argumentos

def suma(num1,num2): #num son los parametros
    resultado = num1 + num2
    return resultado

print(suma(10,10)) #Aqui van los argumentos, el valor que tomara cada variable (Parametros)

#Variables globales

def valores():
    global var1  #global sirve para hacer una variable global
    global var2

    var1 = 110
    var2 = 40
    resultado = var1 + var2
    return resultado

print(valores())

resta = var1 - var2
print(resta)

#Valores indefinidos

def argumento(*num): #Al usar * los elementos ingresados se almacenan en una tupla
    return type(num)

print(argumento(10,9,0))

