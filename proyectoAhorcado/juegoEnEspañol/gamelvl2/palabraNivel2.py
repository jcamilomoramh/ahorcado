from pydoc import describe
import sqlite3 as sql
import random 
def ahorcadoNivel2():
 eleccion = input("[1] start")
 namePlayer = input("Por favor ingrese su nombre: ")
 print("--------------------------------------------------")
 print("Bienvenido al juego del ahorcado "+namePlayer)
 if eleccion == "1":
    conn = sql.connect("datosAhorcado.db")
    cursor = conn.cursor() 
    instruccion = f"SELECT palabra FROM datosNivel2"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    lista = []

    for n in datos:
           process = n 
           for i in process:
             lista.append(i)
             pe = random.choice(lista)  
      
    conn.commit()
    conn.close     
 nivel = 'nivel Medio'   
 name = pe
 palabra = pe       
 conn = sql.connect("datosAhorcado.db")
 cursor = conn.cursor() 
 instruccion = f"SELECT palabra, pista, Descripcion FROM datosNivel2 where palabra = '{name}'"
 cursor.execute(instruccion)
 datos = cursor.fetchall()
 lista = []
 for n in datos:
    process = n 
    for i in process:
        lista.append(i)
 pista = lista[1]
 descrip = lista[2]
 conn.commit()
 conn.close 
 
 errores = 0

 progreso = []
 for i in range(len(palabra)):
    progreso.append("_ ")

 palabra_con_espacios = []
 for char in palabra:
    palabra_con_espacios.append(char + ' ')

 letras_usadas = []

 while errores < 6:
    
    if errores == 0:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print(pista)
    elif errores == 1:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||              |             ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print(pista)
    elif errores == 2:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||              |             ||          ||")
        print("||             -o-            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print('es un animal agil')
    elif errores == 3:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||              |             ||          ||")
        print("||             -o-            ||          ||")
        print("||              |             ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print(pista)
    elif errores == 4:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||              |             ||          ||")
        print("||             -o-            ||          ||")
        print("||             /|\            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print(pista)
    elif errores == 5:
       final =(''.join(progreso))
       conn = sql.connect("datosAhorcado.db")
       cursor = conn.cursor()
       instruccion = f"INSERT INTO reporte (nombre, nivel, errores, palabra, progreso) VALUES ('{namePlayer}','{nivel}','{errores}','{palabra}' ,'{final}' );"
       cursor.execute(instruccion)
       conn.commit()
       conn.close  
       print("+==========================================+")
       print("||                                        ||")           
       print("||              +==============+          ||")
       print("||              |             ||          ||")
       print("||             -o-            ||          ||")
       print("||             /|\            ||          ||")
       print("||             / \            ||          ||")
       print("||                            ||          ||")
       print("||        ::                  ||          ||")
       print("||        ::::::::::::::::::::::          ||")
       print("||          ||             ||             ||")
       print("+==========================================+")
       print(descrip)
       print('Perdiste!')
       
    print(''.join(progreso))
    print("Letras usadas: ", letras_usadas)
    print('Elegi una letra:')
    letra = input()
    if letra in letras_usadas:
        print('Esta letra ya la usaste...')
    else:
        letras_usadas.append(letra)

        hay_error = True
        for i in range(len(palabra)):
            if letra == palabra[i]:
                progreso[i] = letra + ' '
                hay_error = False

        if hay_error:
            errores += 1
        
        if palabra_con_espacios == progreso:
            final =(''.join(progreso))
            conn = sql.connect("datosAhorcado.db")
            cursor = conn.cursor()
            instruccion = f"INSERT INTO reporte (nombre, nivel, errores, palabra, progreso) VALUES ('{namePlayer}','{nivel}','{errores}','{palabra}' ,'{final}' );"
            cursor.execute(instruccion)
            conn.commit()
            conn.close 
            print('Ganaste')
            exit()


def ahorcadoNivel2Ingles():
 eleccion = input("[1] start")
 namePlayer = input("Please enter your name: ")
 print("--------------------------------------------------")
 print("Welcome to game of hanged "+namePlayer)
 print("---------------------------------------------------")
 if eleccion == "1":
    conn = sql.connect("datosAhorcado.db")
    cursor = conn.cursor() 
    instruccion = f"SELECT palabra FROM datosNivel2"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    lista = []

    for n in datos:
           process = n 
           for i in process:
             lista.append(i)
             pe = random.choice(lista)  
      
    conn.commit()
    conn.close     
 nivel = 'level middle'   
 name = pe
 palabra = pe       
 conn = sql.connect("datosAhorcado.db")
 cursor = conn.cursor() 
 instruccion = f"SELECT palabra, pista, Descripcion FROM datosNivel2 where palabra = '{name}'"
 cursor.execute(instruccion)
 datos = cursor.fetchall()
 lista = []
 for n in datos:
    process = n 
    for i in process:
        lista.append(i)
 pista = lista[1]
 descrip = lista[2]
 conn.commit()
 conn.close 
 
 errores = 0

 progreso = []
 for i in range(len(palabra)):
    progreso.append("_ ")

 palabra_con_espacios = []
 for char in palabra:
    palabra_con_espacios.append(char + ' ')

 letras_usadas = []

 while errores < 6:
    
    if errores == 0:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print(pista)
    elif errores == 1:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||              |             ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print(pista)
    elif errores == 2:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||              |             ||          ||")
        print("||             -o-            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print(pista)
    elif errores == 3:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||              |             ||          ||")
        print("||             -o-            ||          ||")
        print("||              |             ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print(pista)
    elif errores == 4:
        print("+==========================================+")
        print("||                                        ||")
        print("||              +==============+          ||")
        print("||              |             ||          ||")
        print("||             -o-            ||          ||")
        print("||             /|\            ||          ||")
        print("||                            ||          ||")
        print("||                            ||          ||")
        print("||        ::                  ||          ||")
        print("||        ::::::::::::::::::::::          ||")
        print("||          ||             ||             ||")
        print("+==========================================+")
        print(descrip)
    elif errores == 5:
       final =(''.join(progreso))
       conn = sql.connect("datosAhorcado.db")
       cursor = conn.cursor()
       instruccion = f"INSERT INTO reporte (nombre, nivel, errores, palabra, progreso) VALUES ('{namePlayer}','{nivel}','{errores}','{palabra}' ,'{final}' );"
       cursor.execute(instruccion)
       conn.commit()
       conn.close  
       print("+==========================================+")
       print("||                                        ||")           
       print("||              +==============+          ||")
       print("||              |             ||          ||")
       print("||             -o-            ||          ||")
       print("||             /|\            ||          ||")
       print("||             / \            ||          ||")
       print("||                            ||          ||")
       print("||        ::                  ||          ||")
       print("||        ::::::::::::::::::::::          ||")
       print("||          ||             ||             ||")
       print("+==========================================+")
       print(descrip)
       print('lost the game!')
       
    print(''.join(progreso))
    print("Letters used: ", letras_usadas)
    print('Choose a letter:')
    letra = input()
    if letra in letras_usadas:
        print('This letter you already used...')
    else:
        letras_usadas.append(letra)

        hay_error = True
        for i in range(len(palabra)):
            if letra == palabra[i]:
                progreso[i] = letra + ' '
                hay_error = False

        if hay_error:
            errores += 1
        
        if palabra_con_espacios == progreso:
            final =(''.join(progreso))
            conn = sql.connect("datosAhorcado.db")
            cursor = conn.cursor()
            instruccion = f"INSERT INTO reporte (nombre, nivel, errores, palabra, progreso) VALUES ('{namePlayer}','{nivel}','{errores}','{palabra}' ,'{final}' );"
            cursor.execute(instruccion)
            conn.commit()
            conn.close 
            print('Win the game')
            exit()