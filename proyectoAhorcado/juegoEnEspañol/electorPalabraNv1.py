from ast import If
import random
from gamelvl1.coco import ahorcadoCoco
from gamelvl1.gato import ahorcadoGato
from gamelvl1.piña import ahorcadoPiña
from gamelvl1.moto import ahorcadoMoto
from gamelvl1.vaca import ahorcadoVaca
def elector():
      eleccion = input("[1] start")
      if eleccion == "1":
       palabras = ["gato","moto", "coco","vaca", "piña"]
       palabra = random.choice(palabras)  

       if palabra == "gato":
         ahorcadoGato()
       elif palabra == "moto":
         ahorcadoMoto()
       elif palabra == "coco":
         ahorcadoCoco()
       elif palabra == "vaca":
        ahorcadoVaca()
       elif palabra == "piña":   
        ahorcadoPiña()
