# Función para desplegar los movimientos realizados
def registros(movimientos, matriz):
    """Esta función recibe la opción de movimientos
    para verificar si quiere que se despliegue la matriz el
    usuario. También recibe la matriz ya con cada uno de los movimientos
    integrados"""
    if movimientos == "Si":
        """Si acepta para la matriz desplegada
        se crea un ciclo para representar los movimientos
        de forma organizada; con un mensaje de salida"""
        i = 1
        print("Aquí están todos los movimientos realizados:")
        for elem in matriz:
            print("Movimiento", i, ":", elem)
            i += 1
        print("Muchas gracias por realizar el programa, ¡agradecemos su visita!")
    else:
        print("Muchas gracias por realizar el programa, ¡agradecemos su visita!")
"""Esta función finalmente regresa o la matriz con un mensaje de
despedida o sólo el mensaje"""

# Función para calcular el pago de electricidad
def cfe(kilowatts):
    """Recibe la cantidad de kilowatts que aparecen
medidor"""
    pago = kilowatts * 0.711
    return pago
    """Regresa el pago de dichos kilowatts"""


# Función para calcular el pago del agua
def cea(personas, litros):
    """Recibe el número de personas de una casa
    y los litros aproximados consumidos"""
    calc_1 = personas * litros
    saldo_1 = calc_1 * 0.03
    "regresa el costo del servicio de agua"
    return saldo_1


# Función para agregar una cuenta
def agregar_cuenta(opcion,forma_de_servicio, calc_gasto):
    """Esta funcion recibe el tipo de servicio, la forma
    y el gasto aproximado que se pretende para la cuenta"""
    if opcion == 1:
        if forma_de_servicio == "vivienda":
            costo_in = 25 * calc_gasto
            costo_t = costo_in * 0.650
            costo_fin = costo_t + 400
            return costo_fin * 1.10
        elif forma_de_servicio == "industrial":
            costo_in = 100 * calc_gasto
            costo_t = costo_in * 0.650
            costo_final = costo_t + 1000
            return costo_final * 1.30
    elif opcion == 2:
        if forma_de_servicio == "vivienda":
            costo_in = 25 * calc_gasto
            costo_t = costo_in * 0.03
            costo_fin = costo_t + 400
            return costo_fin * 1.10
        elif forma_de_servicio == "industrial":
            costo_in = 100 * calc_gasto
            costo_t = costo_in * 0.03
            costo_final = costo_t + 1000
            return costo_final * 1.30
"""En cada condicion regresera un valor siendo el costo final
dependiendo de las opciones a escoger"""

# Función para calcular la cancelación de una cuenta
def cancelacion_cuenta(años,opcion_canc,saldo_pendiente):
    """Recibe como paramteros; los años de servicio,
    la opcion de el servicio a cancelar y el saldo"""
    cuota_cancelacion = 0
    if opcion_canc==1:
        if saldo_pendiente == "si" or saldo_pendiente=="Si":
            cuota_cancelacion = (1.16 * años) + 100+cuota_cancelacion
    elif opcion_canc==2:
        if saldo_pendiente == "si" or saldo_pendiente=="Si":
            cuota_cancelacion=(1.10+años)+150+cuota_cancelacion
    return cuota_cancelacion
"""Regresa la cuota por cancelacion
dependiendo de su saldo"""


# Función para agregar datos personales
def agregar_datos(nombre_completo,edad,codigo_postal,numero_cel):
    """La funcion recibe los datos de la cuenta para guardarlos
en una base que seria la lista a regresar"""
    lista = [nombre_completo, edad, codigo_postal, numero_cel]
    return lista


# Función para crear una matriz de cuentas
def crea_cuenta_matriz(casa, datos, opcion, seccion):
    """Esta funcion crea el movimiento de la creacion
    de cuentas y lo agrega a una lista. los valores a recibir es la casa,
    los datos de la cuenta, la opcion de servicio y
    la seccion."""
    lista = ["Crear cuenta de servicios"]
    if opcion == 1:
        lista.append("CFE")
        lista.append(seccion)
    elif opcion == 2:
        lista.append("CEA")
        lista.append(seccion)
    lista.append(datos)
    return lista
"Regresa la lista con el movimiento creado"


# Función para registrar cancelación de cuenta
def cancel_matriz(opcion_canc, cancelacion, costo_canc):
    """Esta funcion crea el movimiento de cancelacion y lo agrega a
    una lista. Los datos recibidos, son la opcion, el motivo
    y el costo"""
    lista_1 = ["Cancelacion Cuenta"]
    if opcion_canc == 1:
        lista_1.append("CFE")
        lista_1.append(cancelacion)
        lista_1.append(costo_canc)
    elif opcion_canc == 2:
        lista_1.append("CEA")
        lista_1.append(cancelacion)
        lista_1.append(costo_canc)
    return lista_1
"Regresa la lista con el movimiento ya creado"


# Función para checar cuenta
def checar_cuenta_matriz(opcion, cobro, metodo_pago):
    """Crea el movimiento de  checar la cuenta y lo agrega
    a una lista. Los parametros son la opcion de servicio
    el cobro y metodo de pago"""
    lista_2 = ["Checar_Saldo"]
    if opcion == 1:
        lista_2.append("CFE")
        lista_2.append(cobro)
    elif opcion == 2:
        lista_2.append("CEA")
        lista_2.append(cobro)
    lista_2.append(metodo_pago)
    return lista_2
"Regresa lista con movimiento realizado"


# Función para manejar las operaciones de la matriz
def creacion_matriz(casa, matriz, datos, opcion, seccion, cobro,
                    metodo_pago, opcion_canc, cancelacion, costo_canc):
    """Esta funcion recibe todos los parametros
    de movimientos de la funcion y los distribuye dependiendo
    de la opcion."""
    if casa == 1:
        crea_lista = crea_cuenta_matriz(casa, datos, opcion, seccion)
        matriz.append(crea_lista)
    elif casa == 2:
        canc_lista = cancel_matriz(opcion_canc, cancelacion, costo_canc)
        matriz.append(canc_lista)
    elif casa == 3:
        checar_lista = checar_cuenta_matriz(opcion, cobro, metodo_pago)
        matriz.append(checar_lista)
    return matriz
"""Para cada condicion de movimiento manda a llamar
a la funcion respectiva y agrega el movimiento a la matriz"""
matriz = []

# Programa principal
print("Hola, bienvenido a la página oficial del gobierno de pago de "
      +"servicios públicos en línea.")
contador = 0

while contador < 1:
    casa = int(input("Por favor, define el propósito de tu visita:\n"
                     +" 1. Crear cuenta\n"
                     +" 2. Cancelar cuenta\n"
                     +" 3. Checar cuenta.\n"
                     +"Seleccione el número: "))
    if casa < 1 or casa > 3:
        print("Opción inválida. Reinicie el programa.")

    if casa == 1:
        opcion = int(input("Seleccione el servicio:\n 1. CFE\n 2. CEA\n"
                           +"Seleccione el número: "))
        print("Por favor, introduzca la información solicitada.")
        nombre_completo = input("Nombre completo con apellidos: ")
        edad = int(input("Edad en dígitos: "))
        codigo_postal = int(input("Código postal: "))
        numero_cel = int(input(
            "Número celular +52 (si es otro, usted agregue la "
            "digitalización de su país correspondiente): "))
        seccion = input("Seleccione su región:\n Juriquilla\n Corregidora\n"
                        +" Refugio\nEscriba su región: ")

        if opcion == 1:
            corriente = input("Indique si su corriente es de vivienda o industrial: ")
            calculo_gasto = int(input("Ingrese su consumo estimado de energía en kilowatts: "))
            print("El costo de su apertura de cuenta es de: ",
                  "%.3f" % agregar_cuenta(opcion, corriente, calculo_gasto), "pesos")
        elif opcion == 2:
            toma_agua = input("Indique si su toma de agua es de vivienda o industrial: ")
            calculo_gasto = int(input("Ingrese su consumo estimado de agua en metros cúbicos: "))
            print("El costo de su apertura de cuenta es de: "
                  +"%.3f" % agregar_cuenta(opcion, toma_agua, calculo_gasto), "pesos")

        datos = agregar_datos(nombre_completo, edad, codigo_postal, numero_cel)
        print("Datos de su cuenta: ", datos)
        matriz = creacion_matriz(casa, matriz, datos, opcion, seccion, "", "", "", "", "")

    elif casa == 2:
        opcion_canc = int(input("Seleccione el servicio a cancelar:\n 1. CFE\n 2. CEA\n"
                                +"Seleccione el número: "))
        años = int(input("Ingrese los años de servicio: "))
        cancelacion = int(input("Motivo de cancelación: 1. Falla en medidor, "
                                +"2. Cambio de proveedor, 3. Falla de mantenimiento: "))
        saldo_pendiente = str(input("¿Tiene saldo pendiente? (Si/No): "))
        costo_canc = cancelacion_cuenta(años,opcion_canc,saldo_pendiente)
        print("Su cuota de cancelación es:"," %.3f"%costo_canc, "pesos")
        matriz = creacion_matriz(casa, matriz, "", "", "", "", "", opcion_canc, cancelacion, costo_canc)

    elif casa == 3:
        opcion = int(input("Seleccione el servicio a consultar:\n 1. CFE\n 2. CEA\n"
                           "Seleccione el número: "))
        if opcion == 1:
            kw_bajo = float(input("Ingrese la cantidad de kilowatts básico de su recibo: "))
            cobro = cfe(kw_bajo)
            print("La cantidad a pagar es: ","%.3f"% cobro, "pesos")
        elif opcion == 2:
            personas = int(input("Ingrese el número de personas en su casa (En número): "))
            litros = int(input("Ingrese su consumo estimado de agua en litros; "
                               +"Una persona promedio consume 2000-3500 litros mensualmente: "))
            cobro = cea(personas, litros)
            print("El saldo estimado es: ", "%.3f" % cobro, "pesos")

        metodo_pago = input("¿Cómo desea pagar? (Efectivo/Tarjeta): ")
        matriz = creacion_matriz(casa, matriz, "", opcion, "", cobro, metodo_pago, "", "", "")

    reinicio = input("¿Desea realizar otra acción? (Si/No): ")
    if reinicio != "Si":
        contador += 1

# Mostrar todos los movimientos registrados al final
ver_movimientos = input("¿Desea ver todos los movimientos realizados? (Si/No): ")
registros(ver_movimientos, matriz)
