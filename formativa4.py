def menu():
    print("""*** MENU PRINCIPAL ***
          1.- Turistas por país.
          2.- Turista por mes.
          3.- Eliminar turista.
          4.- Salir""")
    opc=(input("Ingrese una opcion:"))
    return opc
def turistas_por_pais(turistas):
    while True:
        pais = input('Ingrese pais a buscar:')
        if pais.isalpha():
            break
        else:
            print('solo letras')
    existe = False
    for clave, datos in turistas.items():
        nombre, pais_turista,clave= datos
        if pais_turista.lower() == pais.lower():
            print(nombre)
            existe = True
    if not existe:
        print("No hay turistas registrados de ese país.")
def turistas_por_mes(turistas):
    while True:
        try:
            mes = int(input("Ingrese el mes (1 al 12): "))
            if 1 <= mes <= 12:
                break
            else:
                print("Debe ser un número entre 1 y 12.")
        except:
            print("Solo números enteros.")
    total = len(turistas)
    cantidad = 0
    for clave, datos in turistas.items():
        fecha = datos[2]
        mes_turista = int(fecha[3:5])
        if mes_turista == mes:
            cantidad += 1
    porcentaje = (cantidad / total) * 100
    print(f"El número de turistas equivale al {round(porcentaje, 1)} % del total.")
def eliminar_turista(turistas):
    nombre = input("Ingrese el nombre del turista a eliminar: ").lower()
    for clave, datos in turistas.items():  
        if datos[0].lower() == nombre:
            del turistas[clave]
            print("Turista eliminado con éxito.")
            return
    print("Turista no encontrado. No se pudo eliminar.")
    