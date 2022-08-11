
from controladorDeNivel import menuNivel,menuNivelIngles
from logAdmin import logADM

def menu():

 print("[1] = Jugar")
 print("[2] = Ingresar como Adimn")
 menu_principal = input()
 if menu_principal=="1":
  menuNivel()
 if menu_principal=="2":
  logADM()
     
def menuIngles():
 print("[1] = Play")
 print("[2] = Login Admin")
 menu_principal = input()
 if menu_principal=="1":
  menuNivelIngles()
 if menu_principal=="2":
  logADM()
            
