#Codigo para verificar 
import sqlite3 as sql
from admin.menuAdmin import menuAdm
def logADM():
  conn = sql.connect('datosAhorcado.db')
  cursor = conn.cursor() 
  instruccion = f"SELECT usuario, password FROM auth;"
  cursor.execute(instruccion)
  datos = cursor.fetchall()
  lista = []

  for n in datos:
    process = n 
    for i in process:
        lista.append(i)
  usur = lista[0]
  contraseña = lista[1]            
  conn.commit()
  conn.close  
  logUsuario = input('Por favor ingrese su usuario: ')
  logPassword = int(input('Por favor ingrese su contraseña: '))
  if logUsuario == usur and logPassword == contraseña:
    menuAdm()
  else:
    print('Credenciales incorrectas.')  
