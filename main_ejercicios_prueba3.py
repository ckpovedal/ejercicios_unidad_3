from ejercicios_para_prueba3 import *

menu = True
while menu: 
    print('*****Interface de afiliados*****')
    print('1. agregar afiliado')
    print('2. buscar afiliado')
    print('3. listar afiliado soltero/a')
    print('4. salir')
    opcion = int(input('ingrese una opción\n'))
    if opcion > 0 and opcion < 5:
        if opcion == 1:
            print("Aregar afiliado")
            agregarafiliado()
        elif opcion == 2:
            print("Buscar Afiliado")
            buscadorafiliado()
        elif opcion == 3:
            print("Listar")
            listarsolteros()
        elif opcion == 4:
            op = int(input("Esta seguro que desea salir?\n1.Si-\n2.No.\n"))
            if op == 1:
                menu = False