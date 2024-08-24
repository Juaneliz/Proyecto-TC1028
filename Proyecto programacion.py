def cfe(a):
    pago= a*0.711
    return(pago)
def cea(b):
    pago_1= b*7.12
    return(pago_1)
def agregar_cuenta(a,b,c,d):
    nombre=a
    colonia=b
    
    
print("Hola, bienvenido a la pagina oficial del gobierno de pago de servicios publicos en linea.")
casa=str(input("Por favor define cual es el proposito de tu visita a la pagina web:\n 1. Crear cuenta para servicios\n 2. Cancelar cuenta\n3. Checar cuenta y servicios.\nPor favor poner el numero del proceso seleccionado:"))
        
if casa==3:
    opcion=int(input("Porfavor escribe el numero del tramite a realizar de los siguientes:\n 1. CFE\n 2. CEA\n 3.Imss\n4.Multas\n Por favor aqui escribe cual es el caso:  "))
    if opcion==1:
        cfe_opciones=int(input("Perfecto,por favor de las siguientes opciones define que quieres realizar:\n 1. Pagar\n 2. Consultar Saldo\n 3. regresar a pregunta principal\n"))
        if cfe_opciones==1:
            cobro=str(input("Por favor escribe aqui de que forma pagaras:\n Tarjeta de debito\n Tarjeta de credito\n Efectivo\nPago:"))
            if cobro=="Tarjeta de debito":
                print("Perfecto, en breve se te dara una cuenta a donde depositar el dinero a traves de transferencia")
        
    elif cfe_opciones==2:
        kw_bajo=float(input("Por favor pon la cantidad de kilowatts basico que se muestran en tu recibo:"))
        print(cfe(kw_bajo),"Es la cantidad a pagar en pesos")
if opcion==2:
    cea_opciones=str(input("Perfecto,por favor de las siguientes opciones define que quieres realizar:\n 1. Pagar\n 2. Consultar Saldo\n 3. regresar a pregunta principal\n"))
    if cea_opciones==2:
        m_cubico=int(input("Escribe aqui por favor cuantos metros cubicos aparecen en el medidor de agua de su vivienda"))
        print(cea(m_cubico),"Es la cantidad a pagar en pesos mexicanos")