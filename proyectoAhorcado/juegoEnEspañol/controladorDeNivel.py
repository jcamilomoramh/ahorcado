
from electorPalabraNv1 import elector


def menuNivel():
  
  namePlayer = input("Por favor ingrese su nombre: ")
  print("--------------------------------------------------")
  print("Bienvenido al juego del ahorcado "+namePlayer)
  print("---------------------------------------------------")
  print("[1] Nivel facil")
  print("[2] Nivel medio")
  print("[3] Nivel dificil")
  nivelDeUuario = input("Por favor ingrese el nivel de dificultad que desea: ")
  if nivelDeUuario == "1":
   elector()
  
 
