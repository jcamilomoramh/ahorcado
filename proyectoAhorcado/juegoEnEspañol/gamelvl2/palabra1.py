def ahorcadoCarro():
 
 palabra = "carro"
 
 errores = 0

 progreso = []
 for i in range(len(palabra)):
    progreso.append("_ ")

 palabra_con_espacios = []
 for char in palabra:
    palabra_con_espacios.append(char + ' ')

 letras_usadas = []

 while errores < 6 or palabra_con_espacios == progreso:
    
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
        print("tiene cola")
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
        print("es un felino ")
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
        print('Es mamifero')
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
        print('Suele dormir en el dia')
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
    if palabra_con_espacios == progreso:
        print("ganaste")   
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
        
       
ahorcadoCarro()