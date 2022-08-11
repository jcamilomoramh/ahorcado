import sqlite3 as sql
from wsgiref.validate import InputWrapper


def menuAdm():
    print('[1] Select Datos')
    print('[2] insert Datos')
    print('[3] Eliminar Datos')
    print('[4] actualizar Tablas')
    print('[5] Salir')
    query = input()
    if query == '1':
       selects()
    if query == '2':
       insertTablanivel1() 
    if query == '3':
       delete()
    if query == '4':
       update()
    if query == '5':
        exit()
   
def selects():

    print('[1] Select en Columna [palabra], [pista], [Descripcion]')
    print('[2] Select en Columna [?], [?]')
    print('[3] Select en Columna [?]')
    print('[4] select en reporte')
    opcion1 = input()
    if opcion1 == '1':
        conn = sql.connect('datosAhorcado.db')
        cursor = conn.cursor()
        table = input('Por favor ingrese la tabla que desea manipular. Recuerde que las tablas a usar son:[datosNivel1],[datosNivel2],[datosNivel3]: ') 
        instruccion = f"Select palabra, pista, Descripcion FROM {table}"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        print('===========================================================')
        print(datos)
        print('===========================================================')
        conn.commit()
        conn.close 
        menuAdm()
    if opcion1 == '2':
        table = input('Por favor ingrese la tabla que desea manipular. Recuerde que las tablas a usar son:[datosNivel1],[datosNivel2],[datosNivel3]: ') 
        print('Por favor ingrese el nombre de las columnas que desea insertar varlores: "palabras","pista","Descripcion"')
        columna1 = input("columna 1: ")
        columna2 = input("columna 2: ")
        conn = sql.connect('datosAhorcado.db')
        cursor = conn.cursor()
        instruccion = f"Select {columna1}, {columna2} FROM {table}"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        print(datos)
        conn.commit()
        conn.close  
        menuAdm()
    if opcion1 == "3":
        table = input('Por favor ingrese la tabla que desea manipular. Recuerde que las tablas a usar son:[datosNivel1],[datosNivel2],[datosNivel3], [reportes]: ') 
        print('Por favor ingrese el nombre de la columna que desea insertar varlores: "palabra","pista","Descripcion"')
        columna1 = input("columna: ")
        conn = sql.connect('datosAhorcado.db')
        cursor = conn.cursor()
        instruccion = f"Select {columna1} FROM {table}"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        print(datos)
        conn.commit()
        conn.close 
        menuAdm()
    if opcion1 == '4':
        conn = sql.connect('datosAhorcado.db')
        cursor = conn.cursor()
        instruccion = f"Select nombre, nivel, errores, palabra, progreso, tiempo Descripcion FROM reporte"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        print('===========================================================')
        print(datos)
        print('===========================================================')
        conn.commit()
        conn.close      
def insertTablanivel1():

    conn = sql.connect('datosAhorcado.db')
    cursor = conn.cursor()
    table = input('Por favor ingrese la tabla que desea manipular. Recuerde que las tablas a usar son:[datosNivel1],[datosNivel2],[datosNivel3], [reportes]: ') 
    palabra = input('Por favor ingrese la palabra que desea agregar al juego.')
    pista = input('Por favor ingrese la Pista que desea para: ')
    descripcion = input('Por favor ingrese descripcion de: ')
    instruccion = f"INSERT INTO {table} VALUES ('{palabra}', '{pista}', '{descripcion}' );"
    cursor.execute(instruccion)
    conn.commit()
    conn.close    
    menuAdm()   
def delete():  
    conn = sql.connect('datosAhorcado.db')
    cursor = conn.cursor()
    table = input('Por favor ingrese la tabla que desea manipular. Recuerde que las tablas a usar son:[datosNivel1],[datosNivel2],[datosNivel3]: ') 
    palabraDelete = input('Por favor ingrese la palabra que desea eliminar junto a su descripcion y pista: ')
    instruccion = f"DELETE FROM {table} WHERE palabra ='{palabraDelete}' ;"
    cursor.execute(instruccion)
    conn.commit()
    conn.close  
    menuAdm() 

def update():
    print('[1] Update en Columna [palabra], [pista], [Descripcion]')
    print('[2] Update en Columna [?], [?]')
    print('[3] Update en Columna [?]')
    opcion1 = input(': ')
    if opcion1 == '1':
     table = input('Por favor ingrese la tabla que desea manipular. Recuerde que las tablas a usar son:[datosNivel1],[datosNivel2],[datosNivel3], [reportes]: ')   
     palabra = input('Por favor ingrese que Palabra desea ingresar: ')
     pista = input('Por favor ingrese que pista desea ingresar: ')
     descripcion = input('Por favor ingrese que descripcion desea ingresar: ')
     idpalabra = input('Por favor ingrese la palabra que a actualizar sus campos: ')
     conn = sql.connect('datosAhorcad.db')
     cursor = conn.cursor()
     instruccion = f"UPDATE {table} SET palabra ='{palabra}', pista='{pista}', descripcion='{descripcion}' WHERE palabra like '{idpalabra}';"
     cursor.execute(instruccion)
     conn.commit()
     conn.close  
     menuAdm() 
    if opcion1 =='2':
     table = input('Por favor ingrese la tabla que desea manipular. Recuerde que las tablas a usar son:[datosNivel1],[datosNivel2],[datosNivel3], [reportes]: ')    
     campo1 = input('Por favor ingrese el dato que desea actualizar: ')   
     newData = input('Por favor ingrese dato nuevo: ')
     campo2 = input('Por favor ingrese el segundo dato que desea actualizar: ')
     newData2 = input('Por favor ingrese dato nuevo del segundo campo: ')
     idpalabra = input('Por favor ingrese la palabra que a actualizar sus campos: ')
     conn = sql.connect('datosAhorcado.db')
     cursor = conn.cursor()
     instruccion = f"UPDATE {table} SET {campo1}='{newData}', {campo2}='{newData2}',  WHERE palabra like '{idpalabra}'"
     cursor.execute(instruccion)
     conn.commit()
     conn.close  
     menuAdm()         
    if opcion1 =='3':
     table = input('Por favor ingrese la tabla que desea manipular. Recuerde que las tablas a usar son:[datosNivel1],[datosNivel2],[datosNivel3], [reportes]: ')    
     campo1 = input('Por favor ingrese el dato que desea actualizar: ')   
     newData = input('Por favor ingrese dato nuevo: ')
     idpalabra = input('Por favor ingrese la palabra que a actualizar sus campos: ')
     conn = sql.connect('datosAhocado.db')
     cursor = conn.cursor()
     instruccion = f"UPDATE {table} SET {campo1}='{newData}'  WHERE palabra like '{idpalabra}'"
     cursor.execute(instruccion)
     conn.commit()
     conn.close  
     menuAdm()    
