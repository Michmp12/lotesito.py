import os

list_urbano= []
list_comercial = []
list_campestre = []
sw = True

def fnt_limpiar():
    os.system('cls')
    print('Autor: Michell Alejandra Mosquera Pacheco')

def fnt_selector(op):
    if op == '1':
        fnt_limpiar()
        categoria_lote = input(' -- CATEGORIA DE LOTE --\n1. Urbano\n2. Comercial\n3. Campestre\n.-> ')
        fnt_limpiar()
        if categoria_lote == '1':
            frente = float(input('Medida del frente del lote: '))
            fondo = float(input('Medida de fondo del lote: '))
            area = frente * fondo
            mt2 = 25000 *  area
            permiso_construccion = 0.45 * mt2
            total = mt2 + permiso_construccion
            lote = f"Area: $ {area} precio del area: $ {mt2} Permiso de la contrucción: $ {permiso_construccion} total: {total}"
            list_urbano.append(lote)
            enter = print('Registro realizado...')
            input('Presione <ENTER> para continuar...')
        
        if categoria_lote == '2':
            frente = float(input('Medida del frente del lote: '))
            fondo = float(input('Medida de fondo del lote: '))
            area = frente * fondo
            mt2 = 60000 *  area
            permiso_construccion = 0.75 * mt2
            total = mt2 + permiso_construccion
            lote = f"Area: $ {area} precio del area: $ {mt2} Permiso de la contrucción: $ {permiso_construccion} total: {total}"
            list_comercial.append(lote)
            enter = print('Registro realizado...')
            input('Presione <ENTER> para continuar...')
        
        if categoria_lote == '3':
            frente = float(input('Medida del frente del lote: '))
            fondo = float(input('Medida de fondo del lote: '))
            area = frente * fondo
            mt2 = 35000 *  area
            permiso_construccion = 0.15 * mt2
            total = mt2 + permiso_construccion
            lote = f"Area: $ {area} precio del area: $ {mt2} Permiso de la contrucción: $ {permiso_construccion} total: {total}"
            list_campestre.append(lote)
            enter = print('Registro realizado...')
            input('Presione <ENTER> para continuar...')
            
        if op == '2':
            categoria_lote = input(' -- CATEGORIA DE LOTE --\n1. Urbano\n2. Comercial\n3. Campestre\n.-> ')
            
            if categoria_lote == '1':
                print(' -- LOTE URBANO --')
                if len(list_urbano) == 0:
                    print('No se encuentran registros...')
                    enter  = input (' Presione <ENTER> para  continuar...')
                else: 
                    for lote in list_urbano:
                        print(lote)
                        
            if categoria_lote == '2':
                print(' -- LOTE COMERCIAL --')
                if len(list_comercial) == 0:
                    print('No se encuentran registros...')
                    enter  = input (' Presione <ENTER> para  continuar...')
                else: 
                    for lote in list_comercial:
                        print(lote)            
        
            if categoria_lote == '3':
                print(' -- LOTE CAMPESTRE --')
                if len(list_campestre) == 0:
                    print('No se encuentran registros...')
                    enter  = input (' Presione <ENTER> para  continuar...')
                else: 
                    for lote in list_campestre:
                        print(lote)

    if op == '3':
        sw == False
while sw == True:
    opcion = input(' --- MENU PRINCIPAL ---\n1. Agregar lotes\n2. Mostrar lotes\n3. Salir\n-> ')
    fnt_selector(opcion)