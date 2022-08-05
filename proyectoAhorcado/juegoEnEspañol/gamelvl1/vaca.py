def ahorcadoVaca():
 
 palabra = "vaca"

 errores = 0

 progreso = []
 for i in range(len(palabra)):
    progreso.append("_ ")

 palabra_con_espacios = []
 for char in palabra:
    palabra_con_espacios.append(char + ' ')

 letras_usadas = []

 while errores < 6 :
    
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
        print("Es un animal con manchas")
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
        print("Es rumiante")
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
        print('Es mamifero')
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
        print('Usamos su leche')
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
        print('Es hervivoro')
    elif errores == 5:
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
       print('Perdiste!')
    elif errores == 6:
       print("Perdiste")       
       errores =+1
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
            print(''.join(progreso))
            print('Ganaste!')