def cfe(a):
    pago= a*0.711
    return(pago)
def cea(a,b):
    calc_1= a*b
    saldo_1=calc_1*0.03
    return(saldo_1)
def agregar_cuenta(opcion,a,b):
    if opcion==1:
        if a=="vivienda":
            costo_in=.5*b
            costo_t=costo_in*0.650
            costo_fin=costo_t+400
            return(costo_fin*1.30)
        elif a=="industrial":
            costo_in=1000*b
            costo_t=costo_in*0.03
            costo_final=costo_t+3500
            return(costo_final*1.30)
    if opcion ==2:
        if a=="vivienda":
            costo_in=1000*b
            costo_t=costo_in*0.03
            costo_fin=costo_t+400
            return(costo_fin*1.30)
        elif a=="industrial":
            costo_in=1000*b
            costo_t=costo_in*0.03
            costo_final=costo_t+3500
            return(costo_final*1.30)
def cancelacion_cuenta(años,cancelacion_luz,saldo_pendiente):
    if cancelacion_luz==1:
        cuota_cancelacion=0
        if saldo_pendiente==1:
            cuota_cancelacion= (1.16*años)+300
        elif saldo_pendiente==2:
            cuota_cancelacion=0
    
    return(cuota_cancelacion)
def agregar_datos(nombre_completo,edad,codigo_postal,numero_cel,):
    lista=[]
    lista.append(nombre_completo)
    lista.append(edad)
    lista.append(codigo_postal)
    lista.append(numero_cel)
    return lista
# Cada litro de agua cuesta 0.03 pesos

print("Hola, bienvenido a la pagina oficial del gobierno de pago de servicios publicos en linea.")
contador=0
while contador<1:
    casa=int(input("Por favor define cual es el proposito de tu visita a la pagina web:\n 1. Crear cuenta para servicios\n 2. Cancelar cuenta\n3. Checar cuenta y servicios.\nPor favor poner el numero del proceso seleccionado:"))
    if casa<=0 or casa>3:
        print("Por favor reinicie el programa, debido a que no tenemos la opcion seleccionada")
    if casa ==1:
        opcion=int(input("Porfavor escribe el numero del servicio que requiere crear a realizar de los siguientes:\n 1. CFE\n 2. CEA\nPor favor aqui escribe el numero del caso:  "))
        print("Perfecto, te tomaremos una serie de datos para tener un usuario de cuenta preparado")
        nombre_completo=str(input("Nombre completo con apellidos"))
        edad=int(input("Edad en digitos"))
        codigo_postal=int(input("Codigo postal:"))
        numero_cel=int(input("Numero celular +52(si es otro usted agregue la digitalizacion de su pais correspondeinte)"))
        print("Perfecto, por favor dinnos en que region de las siguientes te encuentras: \n Juriquilla \n Corregidora \n Refugio")
        seccion=str(input("Porfavor aqui escribe la region como esta escrita en el programa:"))
        if opcion ==1:           
            if seccion=="Juriquilla":
                corriente=str(input("Digannos si su corriente es de vivienda o industrial."))
                calculo_gasto=int(input("Por favor, en promedio como cuanto supone en consumir de energia en kilowatts\n(persona promedio consume aproximadamente entre 250-400kw al mes):"))
                print("El costo de su apertura de cuenta es de:","%.3f"%agregar_cuenta(opcion,corriente,calculo_gasto),"pesos")
            elif seccion=="Corregidora":
                corriente=str(input("Digannos si su toma de agua es de vivienda o industrial."))
                calculo_gasto1=int(input("Por favor, en promedio como cuanto supone en consumir de energia en kilowatts\n(persona promedio consume aproximadamente entre 250-400kw al mes):"))
                costo_corregidora=agregar_cuenta(opcion,corriente,calculo_gasto1)
                print("El costo de su apertura de cuenta es de:",costo_corregidora,"pesos")
            elif seccion=="Refugio":
                corriente=str(input("Digannos si su toma de agua es de vivienda o industrial."))
                calculo_gasto1=int(input("Por favor, en promedio como cuanto supone en consumir de energia en kilowatts\n(persona promedio consume aproximadamente entre 250-400kw al mes):"))
                costo_refugio=agregar_cuenta(opcion,corriente,calculo_gasto1)
                print("El costo de su apertura de cuenta es de:",costo_refugio,"pesos")
            datos=agregar_datos(nombre_completo,edad,codigo_postal,numero_cel)
            print("Perfecto sus datos de su cuenta son los siguientes",datos)
            reinicio=str(input("Si desea realizar otra accion escriba Si. De lo contrario escriba No"))
            if reinicio=="Si":
                contador=0
            else:
                contador=contador+1
            
        if opcion == 2:            
            if seccion=="Juriquilla":
                toma_agua=str(input("Digannos si su toma de agua es de vivienda o industrial."))
                calculo_gasto=int(input("Por favor, en promedio como cuanto supone en consumir de agua en metros cubicos\n(1 metro cubico=1000litros):"))
                print("El costo de su apertura de cuenta es de:","%.3f"%agregar_cuenta(opcion,toma_agua,calculo_gasto),"pesos")
            elif seccion=="Corregidora":
                toma_agua1=str(input("Digannos si su toma de agua es de vivienda o industrial."))
                calculo_gasto1=int(input("Por favor, en promedio como cuanto supone en consumir de agua en metros cubicos\n(1 metro cubico=1000litros):"))
                costo_corregidora=agregar_cuenta(opcion,toma_agua1,calculo_gasto1)
                print("El costo de su apertura de cuenta es de:",costo_corregidora,"pesos")
            elif seccion=="Refugio":
                toma_agua1=str(input("Digannos si su toma de agua es de vivienda o industrial."))
                calculo_gasto1=int(input("Por favor, en promedio como cuanto supone en consumir de agua en metros cubicos\n(1 metro cubico=1000litros):"))
                costo_refugio=agregar_cuenta(opcion,toma_agua1,calculo_gasto1)

                print("El costo de su apertura de cuenta es de:",costo_refugio,"pesos")
            datos=agregar_datos(nombre_completo,edad,codigo_postal,numero_cel)
            print("Perfecto sus datos de su cuenta son los siguientes",datos)
            reinicio=str(input("Si desea realizar otra accion escriba Si. De lo contrario escriba No"))
            if reinicio=="Si":
                contador=0
            else:
                contador=contador+1
    elif casa==2:
        c=0
        while c<1:
            opcion_canc=int(input("Porfavor escribe el numero de servicio que requiere cancelar de los siguientes:\n 1. CFE\n 2. CEA\nPor favor aqui escribe cual es el caso:  "))
            if opcion_canc==1:
                años=int(input("Cuantos años de servicio de contrato ha estado con nosotros:"))
                cancelacion_luz=int(input("Defina cual es el motivo de su cancelacion de los posteriores: Falla en medidor(1)\nCambio de proovedor(2)\nFalla de mantenimiento(3)\nEscriba aqui:"))
                saldo_pendiente=int(input("La cuota de cancelacion dependera de su saldo pendiente en su servicio.\nEscriba aqui si tiene saldo pendiente o no\nSi(1)\nNo(2)\n:):"))
                print(cancelacion_cuenta(años,cancelacion_luz,saldo_pendiente),"Sera su cuota designada")
                c=c+1
            if opcion_canc==2:
                años=int(input("Cuantos años de servicio de contrato ha estado con nosotros:"))
                cancelacion_luz=int(input("Defina cual es el motivo de su cancelacion de los posteriores: Falla en medidor(1)\nCambio de proovedor(2)\nFalla de mantenimiento(3)\nEscriba aqui:"))
                saldo_pendiente=int(input("La cuota de cancelacion dependera de su saldo pendiente en su servicio.\nEscriba aqui si tiene saldo pendiente o no\nSi(1)\nNo(2)\n:):"))
                print(cancelacion_cuenta(años,cancelacion_luz,saldo_pendiente),"Sera su cuota designada")
                c=c+1
                 
        reinicio=str(input("Si desea realizar otra accion escriba Si. De lo contrario escriba No"))
        if reinicio=="Si":
            contador=0
        else:
            contador=contador+1
    elif casa==3:
        opcion=int(input("Porfavor escribe el numero del tramite a realizar de los siguientes:\n 1. CFE\n 2. CEA\nPor favor aqui escribe cual es el caso:  "))
        if opcion==1:
            cfe_opciones=int(input("Perfecto,por favor de las siguientes opciones define que quieres realizar:\n 1. Pagar\n 2. Consultar Saldo\n 3. regresar a pregunta principal\n"))
            if cfe_opciones==1:
                cobro=str(input("Por favor escribe aqui de que forma pagaras:\n Tarjeta de debito\n Tarjeta de credito\n Efectivo\nPago:"))
                if cobro=="Tarjeta de debito":
                    print("Perfecto, en breve se te dara una cuenta a donde depositar el dinero a traves de transferencia")
                elif cobro=="Efectivo":
                    print("Acuda al oxxo, sucursal de CFE; a realizar su pago")
                
            elif cfe_opciones==2:
                kw_bajo=float(input("Por favor pon la cantidad de kilowatts basico que se muestran en tu recibo:"))
                print(cfe(kw_bajo),"Es la cantidad a pagar en pesos")
            reinicio=str(input("Si desea realizar otra accion escriba Si. De lo contrario escriba No"))
            if reinicio=="Si":
                contador=0
            else:
                contador=contador+1
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
            reinicio=str(input("Si desea realizar otra accion escriba Si. De lo contrario escriba No"))
            if reinicio=="Si":
                contador=0
            else:
                contador=contador+1
print("Muchas gracias por realizar el programa, agradecemos su visita, regrese pronto!!!")
