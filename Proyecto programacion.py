def cfe(a):
    pago= a*0.711
    return(pago)
def cea(a,b):
    calc_1= a*b
    saldo_1=calc_1*0.03
    return(saldo_1)
def agregar_cuenta_cea(a,b):
    if a=="vivienda":
        costo_in=1000*b
        costo_t=costo_in*0.03
        costo_fin=costo_t+400
        return(costo_fin)
    elif a=="industrial":
        costo_in=1000*b
        costo_t=costo_in*0.03
        costo_final=costo_t+3500
        return(costo_final)
def agregar_cuenta_impuestos(a,b):
    cuenta=1.16*a
    cuenta1=(cuenta+b)/2
    return(cuenta1)

    
# Cada litro de agua cuesta 0.03 pesos
    
    
print("Hola, bienvenido a la pagina oficial del gobierno de pago de servicios publicos en linea.")
casa=int(input("Por favor define cual es el proposito de tu visita a la pagina web:\n 1. Crear cuenta para servicios\n 2. Cancelar cuenta\n3. Checar cuenta y servicios.\nPor favor poner el numero del proceso seleccionado:"))
if casa<=0 or casa>3:
    print("Por favor reinicie el programa, debido a que no tenemos la opcion seleccionada")
if casa ==1:
    opcion=int(input("Porfavor escribe el numero del tramite a realizar de los siguientes:\n 1. CFE\n 2. CEA\n 3.Impuestos\nPor favor aqui escribe el numero del caso:  "))
    print("Perfecto, por favor dinnos en que region de las siguientes te encuentras: \n Juriquilla \n Corregidora \n Refugio")
    seccion=str(input("Porfavor aqui escribe la region como esta escrita en el programa:"))
    if opcion == 2:
        if seccion=="Juriquilla":
            toma_agua=str(input("Digannos si su toma de agua es de vivienda o industrial."))
            calculo_gasto=int(input("Por favor, en promedio como cuanto supone en consumir de agua en metros cubicos\n(1 metro cubico=1000litros):"))
            print("El costo de su apertura de cuenta es de:","%.3f",agregar_cuenta_cea(toma_agua,calculo_gasto),"pesos")
        elif seccion=="Corregidora":
            toma_agua1=str(input("Digannos si su toma de agua es de vivienda o industrial."))
            calculo_gasto1=int(input("Por favor, en promedio como cuanto supone en consumir de agua en metros cubicos\n(1 metro cubico=1000litros):"))
            costo_corregidora=agregar_cuenta_cea(toma_agua1,calculo_gasto1)
            costo=costo_corregidora*1.30
            print("El costo de su apertura de cuenta es de:",costo,"pesos")
        elif seccion=="Refugio":
            toma_agua1=str(input("Digannos si su toma de agua es de vivienda o industrial."))
            calculo_gasto1=int(input("Por favor, en promedio como cuanto supone en consumir de agua en metros cubicos\n(1 metro cubico=1000litros):"))
            costo_corregidora=agregar_cuenta_cea(toma_agua1,calculo_gasto1)
            costo=costo_corregidora*1.30
            print("El costo de su apertura de cuenta es de:",costo,"pesos")
if casa==2:
    opcion_canc=int(input("Porfavor escribe el numero del tramite a realizar de los siguientes:\n 1. CFE\n 2. CEA\n 3.Impuestos\nPor favor aqui escribe cual es el caso:  "))
    if opcion_canc==1:
        cancelacion_luz=int(input("Defina cual es el motivo de su cancelacion de los posteriores: Falla en medidor(1)\nCambio de luz(2)\nFalla de mantenimiento(3)"))
        
        
if casa==3:
    opcion=int(input("Porfavor escribe el numero del tramite a realizar de los siguientes:\n 1. CFE\n 2. CEA\n 3.Impuestos\nPor favor aqui escribe cual es el caso:  "))
    if opcion==1:
        cfe_opciones=int(input("Perfecto,por favor de las siguientes opciones define que quieres realizar:\n 1. Pagar\n 2. Consultar Saldo\n 3. regresar a pregunta principal\n"))
        if cfe_opciones==1:
            cobro=str(input("Por favor escribe aqui de que forma pagaras:\n Tarjeta de debito\n Tarjeta de credito\n Efectivo\nPago:"))
            if cobro=="Tarjeta de debito":
                print("Perfecto, en breve se te dara una cuenta a donde depositar el dinero a traves de transferencia")
        elif cfe_opciones==2:
            kw_bajo=float(input("Por favor pon la cantidad de kilowatts basico que se muestran en tu recibo:"))
            print(cfe(kw_bajo),"Es la cantidad a pagar en pesos")
    elif opcion==2:
        cea_opciones=int(input("Perfecto,por favor de las siguientes opciones quiere realizar:\n 1. Consultar Saldo\n 2.Pago\n "))
        if cea_opciones==1:
            personas=int(input("Escribe aqui por favor cuantas personas se encuentran en tu casa"))
            litros=int(input(" En promedio una persona gasta 6000 litros al mes, Escribe aqui la cantidad estimada de consumo en litros"))
            print("%.3f"%cea(personas,litros),"Es la cantidad estimada de saldo en pesos mexicanos")
            print("Quiere proceder a pagar el saldo??")
            pago=int(input("Escriba 1 para proceder a pagar y 2 para regresar a la pagina:"))
            #Esto se hara desoues porque me falta una herramienta para realizarlo.
            if pago==1:
                print("Perfecto, en breve le mandaremos informacion ")

