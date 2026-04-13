#--------Trabajo Final: Banco sencilo---------------
from funciones import nombre, num_positivos, Menu, num, num_menos
# Diccionario principal: almacena el nombre como 'llave' y otro diccionario con el saldo como 'valor'
usuario = {}
opcion = 0 
# Bucle principal que mantiene el programa funcionando hasta que elijas la opción 7
while opcion != 7:
    opcion = Menu()
    
    # --- OPCIÓN 1: REGISTRO ---
    if opcion == 1:
        nombre_titular = nombre()  # Llama a la función que valida el texto
        # Verifica si el nombre ya ha sido usado para no sobrescribir datos
        if nombre_titular in usuario:
            print('No se vale ingresar nombres repetidos.')
            print('-'*77)
        else:
            saldo_inicial = num_positivos()  # Pide y valida el saldo inicial
            # Guarda los datos usando una estructura de diccionario anidado
            usuario[nombre_titular] = {'Saldo': saldo_inicial}
            print(f'Cuenta registrada correctamente para {nombre_titular}.')
            print(f'Saldo inicial: {saldo_inicial}')
            print('-'*77)

    # --- OPCIÓN 2: LISTAR CUENTAS ---
    elif opcion == 2:
        if usuario:  # Verifica si el diccionario tiene algún dato
            print('-----Listado de clientes-----')
            # Recorre el diccionario obteniendo tanto el nombre como el saldo
            for nombre_titular, saldo in usuario.items():      
                print(f'{nombre_titular} -> Saldo: {saldo["Saldo"]}')
                print('-'*77)
        else:
            print('No hay usuarios registrados.')
            print('-'*77)

    # --- OPCIÓN 3: CONSULTA INDIVIDUAL ---
    elif opcion == 3:
        if usuario:
            busqueda = nombre()
            # Búsqueda directa por llaves
            if busqueda in usuario:
                print(f"El saldo de {busqueda} es: {usuario[busqueda]['Saldo']}")
                print('-'*77)
            else:
                print('El usuario no esta registrado.')
                print('-'*77)
        else:
            print('No hay usuarios registrados.')
            print('-'*77)

    # --- OPCIÓN 4: DEPÓSITOS ---
    elif opcion == 4:
        if usuario:
            busqueda = nombre()
            if busqueda in usuario:
                valor_ingresar = num()  # Valida que el depósito sea un número positivo
                # Actualiza el valor sumando directamente al saldo existente
                usuario[busqueda]['Saldo'] += valor_ingresar
                print('Deposito realizado con éxito.')
                print(f"El saldo de {busqueda} es: {usuario[busqueda]['Saldo']}")
                print('-'*77)
            else:
                print('El usuario no esta registrado.')
                print('-'*77)
        else:
            print('No hay usuarios registrados.')
            print('-'*77)

    # --- OPCIÓN 5: RETIROS ---
    elif opcion == 5:
        if usuario:
            busqueda = nombre()
            if busqueda in usuario:
                valor_ingresar = num_menos()
                # Validación de fondos: evita que el usuario retire más de lo que posee
                if valor_ingresar > usuario[busqueda]['Saldo']:
                    print('El valor ingresado es mayor al que tiene en la cuenta.')
                    print('-'*77)
                else:
                    # Resta el monto del saldo del usuario específico
                    usuario[busqueda]['Saldo'] -= valor_ingresar
                    print('Retiro realizado con éxito.')
                    print(f"El saldo de {busqueda} es: {usuario[busqueda]['Saldo']}")
                    print('-'*77)   
            else:
                print('El usuario no esta registrado.')
                print('-'*77)
        else:
            print('No hay usuarios registrados.')
            print('-'*77)

    # --- OPCIÓN 6:MAYOR SALDO---
    elif opcion == 6:
        if usuario: 
            # Crea una lista solo con los saldos para encontrar el valor máximo
            saldos = [v['Saldo'] for v in usuario.values()]
            mayor_saldo = max(saldos)
            # Busca quién o quiénes coinciden con ese saldo máximo
            for nombre_titular, v in usuario.items():
                if v['Saldo'] == mayor_saldo:
                    print(f"La cuenta con saldo mas alto es de {nombre_titular} con un saldo de: {mayor_saldo}")
                    print('-' *77)
        else:
            print('No hay usuarios registrados.')
            print('-' * 77)

print('Saliendo.......')
