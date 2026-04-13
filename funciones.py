def nombre():
    # Bucle infinito hasta que el usuario ingrese un nombre válido
    while True:
        nombre_titular = input('Ingresa el nombre -> ').strip().title()
        
        if nombre_titular == '':
            print('No se permite vacío.')
        
        elif any(len(nombre) <= 2  for nombre in nombre_titular.split()):
            print('Su nombre es muy corto.')

            # .isalpha() asegura que solo se hayan ingresado letras (sin números ni símbolos)
        elif not nombre_titular.replace(" ", "").isalpha():
            print('No se permiten números ni caracteres especiales.')

        else:
            return nombre_titular # Retorna el nombre y rompe el ciclo
      

def num_positivos():
    while True:
        saldo_inicial = input('Ingrese su saldo -> ')
        # .isdigit() verifica que el texto ingresado pueda ser un numero número entero
        try:
            saldo_inicial = float(saldo_inicial)
            if saldo_inicial >= 0:
                return saldo_inicial
            else:
                 print('Debse ser mayor o igual a cero.')
        except:
            print('Solo se valen números enteros o decimales.')
        
       

def Menu():
    while True:
        # Menú visual usando triple comilla para mantener el formato de varias líneas
        opcion = input('''
−−−−− MENU −−−−−
1. Registrar cuenta
2. Mostrar cuentas
3. Consultar saldo
4. Depositar dinero
5. Retirar dinero
6. Mostrar mayor saldo
7. Salir
-> ''')

        # Validaciónes: debe ser número y estar en el rango del 1 al 7
        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 7:
            print('Opción inválida.')
        else:
            return int(opcion)

def num():
    # Función específica para depósitos (valida que sea mayor a 0)
    while True:
        saldo_inicial = input('Ingrese su saldo -> ')
        # .isdigit() verifica que el texto ingresado pueda ser un numero número entero
        try:
            saldo_inicial = float(saldo_inicial)
            if saldo_inicial > 0:
                return saldo_inicial
            else:
                 print('Debse ser mayor a cero.')
        except:
            print('Solo se valen números enteros o decimales.')

def num_menos():
    # Función específica para retiros (valida que sea mayor a 0)
    while True:
        saldo_inicial = input('Ingrese su saldo -> ')
        # .isdigit() verifica que el texto ingresado pueda ser un numero número entero
        try:
            saldo_inicial = float(saldo_inicial)
            if saldo_inicial > 0:
                return saldo_inicial
            else:
                 print('Debse ser mayor a cero.')
        except:
            print('Solo se valen números enteros o decimales.')

