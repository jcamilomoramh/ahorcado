import sqlite3 as sql
import sys
from unicodedata import name
sys.path.append("/")
import random

def createDB():
    conn = sql.connect("datosAhorcado.db")
    conn.commit()
    conn.close()
def createTable():
    conn = sql.connect("datosAhorcado.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE report(
              nombre text(17) not null,
              errores int(1),
              palabra text(8),
              tiempo  time(9)
        ) ;"""
    )
    
    conn.commit()
    conn.close
def insert():
    conn = sql.connect("datosAhorcado.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO auth (usuario, password) VALUES ('admin', 12345678 );"
    cursor.execute(instruccion)
    conn.commit()
    conn.close 
def selectData():    
  conn = sql.connect("datosAhorcado.db")
  cursor = conn.cursor() 
  instruccion = f"SELECT usuario, password FROM auth"
  cursor.execute(instruccion)
  datos = cursor.fetchall()
  lista = []

  for n in datos:
    process = n 
    for i in process:
        lista.append(i)
  usur = lista[0]
  contraseña = lista[1]      
  print(usur,contraseña)      
  conn.commit()
  conn.close         
def selectFilas(): 
  name = 'coco'       
  conn = sql.connect("datosAhorcado.db")
  cursor = conn.cursor() 
  instruccion = f"SELECT palabra, pista, Descripcion FROM datosNivel1 where palabra = '{name}'"
  cursor.execute(instruccion)
  datos = cursor.fetchall()
  lista = []
  for n in datos:
    process = n 
    for i in process:
        lista.append(i)
  pe = lista[1]
  per = lista[2]
  print(pe,per)      
  conn.commit()
  conn.close           
if __name__ == "__main__":
   selectFilas()