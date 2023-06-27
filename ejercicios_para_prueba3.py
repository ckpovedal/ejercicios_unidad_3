#No funciona bien aun

#la lista para almacenar
afiliados = []

# funciones para validar el rut
def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "")
    if len(rut) < 2:
        return False
    cuerpo = rut[-1]
    dv = rut[-1].upper()
    suma = 0
    multiplo = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplo
        multiplo += 1 
        if multiplo == 8:
            multiplo = 2
    resulta = 11 - (suma % 11)
    if resultado == 11:
        resultado = "0"
    elif resultado == 10:
        resultado = "K"
    else:
        resultado = str(resultado)
    return resultado == dv 

# Función para grabar los datos de una persona
def agregarafiliado():
    rut = input("Ingrese el rut de la persona:\n")
    while not validar_rut(rut):
        print("Rut inválido, intente nuevamente.")
        rut = input("Ingrese el rut de la persona:\n")
    
    nombre = input("Ingrese el nombre de la persona:\n")
    edad = int(input("Ingrese la edad de la persona:\n"))
    while edad <= 18:
        print("La edad debe ser mayor a 18 años, intente nuevamente.")
        edad = int(input("Ingrese la edad de la persona:\n"))

    estado_civil = input("Ingrese el estado civil de la persona (C = Casado, S = Soltero, V = Viudo)\n")
    while estado_civil not in ['C', 'S', 'V']:
        print("Estado civil inválido, intente nuevamente.")
        estado_civil = input("Ingrese el estado civil de la persona (C = Casado, S = Soltero, V = Viudo)\n")

    fecha_afiliacion = input("Ingrese la fecha de afiliación de la persona:\n")

    afiliado = {
        'Rut' : rut,
        'Nombre' : nombre,
        'Edad' : edad,
        'Estado civil' : estado_civil,
        'Fecha de afiliacion' : fecha_afiliacion
    }
    afiliados.append(afiliado)
    print("Registro almacenado exitosamente.")


# Funcion para buscar una persona por su rut
def buscadorafiliado():
    encontrado = False
    for afiliado in afiliados:
        if afiliado['Rut'] == rut:
            print("---- Información de la persona ----")
            print("Rut: ", afiliado['Rut'])
            print("Nombre: ", afiliado['Nombre'])
            print("Edad:", afiliado['Edad'])
            print("Estado civil: ", afiliado['Estado civil'])
            print("Fecha de afiliación: ", afiliado['Fecha de afiliación'])
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ninguna persona con ese rut.")

#Funcion para listar unicamente solteros
def listarsolteros():
    print('Incompleta')
    

