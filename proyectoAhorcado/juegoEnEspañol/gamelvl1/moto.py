def ahorcadoMoto():
 
 palabra = "moto"

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
        print("Vehiculo de uso personal")
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
        print("puede llevar maximo dos personas")
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
        print('Tiene dos ruedas')
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
        print('Es una forma rapida de trasportarse')
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
        print('Suele ser mala opcion de trasportarse en dias lluviosos')
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
          