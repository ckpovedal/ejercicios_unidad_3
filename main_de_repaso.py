from ejercicios_de_repaso_funciones import *
import time

#print(resta(30, 10))

#print(resta(b=30, a=10))

#frase = funcion()
#print(frase)

#print(resta1())

#datos = [10000, 10]
#print("El monto final a pagar es: ", calculo(*datos))

#saludo(mensaje="Buen día", nombre="Pedro")


#Ejercicio Menú calculos

menu = "******Calculos******\n- Opciones:\n1. Calcular Iva.\n2. Calcular descuento de un producto.\n3. Calcular su IMC.\n4. No hacer nada."
sw = True
while sw:
    print(menu)
    try:
        op = int(input("Ingrese una opción\n"))
        if op > 0 and op <= 4:
            if op == 1:
                precio=int(input("Ingrese el precio a calcular IVA\n"))
                print("El iva es: ", calcular_iva(precio))
                time.sleep(3)
                sw = False
            elif op == 2:
                precio=int(input("Ingrese el precio del producto\n"))
                descuento=float(input("Ingrese el descuento en decimal\n"))
                precio_final = calculo(precio, descuento)
                print("El valor final de su producto con descuento es: ", precio_final)
                time.sleep(3)
                sw = False 
            elif op == 3:
                peso = float(input("Ingrese su peso en kilogramos\n"))
                estatura = float(input("Ingrese su estatura en metros\n"))
                imc = calcular_imc(peso, estatura)
                print("Su IMC es :", imc)
                time.sleep(3)
                sw = False
            elif op == 4:
                print("Hasta pronto")
                time.sleep(5)
                sw = False
        else:
            print("Ingrese una opción Valida")
            time.sleep(3)
    except:
        print("Dato inválido, vuelva a ingresar")
        time.sleep(5)



