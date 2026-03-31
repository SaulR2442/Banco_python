def nombre():
    while True:
        nombre_titular = input('Ingresa el nombre -> ')
        
        if nombre_titular == '':
            print('No se permite vacío.')
        
        elif not nombre_titular.isalpha():
            print('No se permiten números ni caracteres especiales.')
        
        else:
            return nombre_titular


def num_positivos():
    while True:
        saldo_inicial = input('Ingrese su saldo -> ')
        
        if not saldo_inicial.isdigit():
            print('Solo se permiten números.')
        elif int(saldo_inicial) < 0:
            print('Debe ser mayor  o igual a 0.')
        else:
            return int(saldo_inicial)
def Menu():
    while True:
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

        if not opcion.isdigit():
            print('Solo números.')
        elif int(opcion) < 1 or int(opcion) > 7:
            print('Opción inválida.')
        else:
            return int(opcion)


def num():
    while True:
        saldo_inicial = input('Ingrese lo que quiere depositar -> ')
        
        if not saldo_inicial.isdigit():
            print('Solo se permiten números.')
        elif int(saldo_inicial) <= 0:
            print('Debe ser mayor a 0.')
        else:
            return int(saldo_inicial)

def num_menos():
    while True:
        saldo_inicial = input('Ingrese lo que quiere retirar -> ')
        
        if not saldo_inicial.isdigit():
            print('Solo se permiten números.')
        elif int(saldo_inicial) <= 0:
            print('Debe ser mayor a 0.')
        else:
            return int(saldo_inicial)

       