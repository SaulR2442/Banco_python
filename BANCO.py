from funciones import nombre,num_positivos,Menu,num,num_menos

usuario = {}

opcion = 0

while opcion != 7 :

    opcion = Menu()
    

    if opcion == 1:
        nombre_titular = nombre()
        saldo_inicial = num_positivos()
        if nombre_titular in usuario:
            print ('No se vale ingresar nombres, repetidos.')
            print('-'*77)
        else:
            usuario[nombre_titular] = {'Saldo': saldo_inicial}
            print(f'Cuenta registrada correctamente para {nombre_titular}.')
            print(f'Saldo inicial: {saldo_inicial}')
            print('-'*77)


    elif opcion == 2:
        if not usuario == {}:  
            for nombre,saldo in usuario.items():      
                print(f'{nombre} -> Saldo: {saldo["Saldo"]}')
                print('-'*77)
        else:
            print('No hay usuarios registrados.')
            print('-'*77)


    elif opcion == 3:
        if not usuario == {}:
            busqueda = nombre()
            if busqueda in usuario:
                    print(f"El saldo de {busqueda} es: {usuario[busqueda]['Saldo']}")
                    print('-'*77)
            else:
                print('El usuario no esta registrado.')
                print('-'*77)
        else:
            print('No hay usuarios registrados.')
            print('-'*77)


    elif opcion == 4:
        if not usuario == {}:
            busqueda = nombre()
            valor_ingresar = num()
            if busqueda in usuario:
                usuario[busqueda]['Saldo'] += valor_ingresar
                print('Deposito realizado con éxito.')
                print(f"El saldo de {busqueda} es: {usuario[busqueda]['Saldo']}")
            else:
                print ('No se encontro')
                print('-'*77)
        else:
            print('No hay usuarios registrados.')
            print('-'*77)


    elif opcion == 5:
        if not  usuario == {}:
            busqueda = nombre()
            valor_ingresar = num_menos()
            if busqueda in usuario:
                if valor_ingresar >  usuario[busqueda]['Saldo']:
                    print('El valor ingresado es mayor al que tiene en la cuenta.')
                    print('-'*77)
                else:
                    usuario[busqueda]['Saldo'] -= valor_ingresar
                    print('Retiro realizado con éxito.')
                    print(f"El saldo de {busqueda} es: {usuario[busqueda]['Saldo']}")
                    print('-'*77)   
            else:
                print ('No se encontro')
                print('-'*77)
        else:
            print('No hay usuarios registrados.')
            print('-'*77)


    elif opcion == 6:
        if not usuario == {}: 
            saldos = [v['Saldo'] for v in usuario.values()]
            mayor_saldo = max(saldos)
            for nombre_titular, v in usuario.items():
                if v['Saldo'] == mayor_saldo:
                    print(f"La cuenta con saldo es de {nombre_titular} con: {mayor_saldo}")
            print('-' *77)
        else:
            print('No hay usuarios registrados.')
            print('-' * 77)


print('Saliendo.......')           

                

            