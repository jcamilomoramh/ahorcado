#Menu de eleccion de nivel

from gamelvl1.palabraNivel1 import ahorcadoNivel1, ahorcadoNivel1Ingles
from gamelvl2.palabraNivel2 import ahorcadoNivel2, ahorcadoNivel2Ingles
from gamelvl3.palabraNivel3 import ahorcadoNvl3,ahorcadoNivel3Ingles
import sqlite3 as sql



def menuNivel():
  print("---------------------------------------------------")
  print("[1] Nivel facil")
  print("[2] Nivel medio")
  print("[3] Nivel dificil")
  nivelDeUuario = input("Por favor ingrese el nivel de dificultad que desea: ")
  if nivelDeUuario =='1':
    ahorcadoNivel1()
  if nivelDeUuario == '2':
    ahorcadoNivel2()
  if nivelDeUuario == '3':
    ahorcadoNvl3()    
    
def menuNivelIngles():
  print("[1] Level easy")
  print("[2] Level middle")
  print("[3] Nivel hard")
  nivelDeUuario = input("Please write the level that you want play: ")
  if nivelDeUuario =='1':
    ahorcadoNivel1Ingles()
  if nivelDeUuario == '2':
    ahorcadoNivel2Ingles()
  if nivelDeUuario == '3':
    ahorcadoNivel3Ingles()        
  

