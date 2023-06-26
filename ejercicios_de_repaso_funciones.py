def resta(a, b):
    return a - b

def funcion():
    return "Bienvenidos a Python"

def resta1(a=None, b=None):
    if a == None or b == None:
        print("Error. faltan parámentros a la función")
        return
    return a - b

def calculo(precio, descuento):
    precio_final = precio - (precio * descuento) 
    return precio_final

def saludo(nombre, mensaje='Python'):
    print(mensaje, nombre)

def calcular_iva(precio):
    return precio * 0.19

def calcular_imc(peso, estatura):
    if peso == None or estatura == None:
        print("Error, faltan datos para hacer el calculo de su IMC")
    else: imc = peso / estatura ** 2
    if imc < 18.5:
        print("Usted esta bajo peso")
        return imc
    elif imc > 18.5 and imc <= 24.9:
        print("Usted esta dentro del peso adecuado")
        return imc
    elif imc > 25.0 and imc <=29.9:
        print("Usted esta con sobrepeso")
        return imc
    elif imc > 30.0 and imc <= 34.9:
        print("Usted esta con obesidad grado 1")
        return imc
    elif imc > 34.0: 
        print("Usted esta con obesidad grado 2")
        return imc
    
