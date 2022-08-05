

from controladorDeNivel import menuNivel
from controllers import createDB

def menu():

 print("[1] = Jugar")
 print("[2] = cambiar lenguaje/change lenaguage")
 print("[3] = Login Adimn")
 menu_principal = input()
 if menu_principal=="1":
  menuNivel()
menu()
            
