

from menu import menu, menuIngles

def idiomaJuego():
    print("[1] español/spanish")
    print("[2] english/ingles")
    idiomaSeleccion = input("")
    if idiomaSeleccion == "1":
        menu()
    if idiomaSeleccion == "2":
        menuIngles()    
