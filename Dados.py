#Sánchez Medina Paola Guadalupe
#Juego de dados Craps en python

import random
import os

#Variables
op = 1
juego = 1

#Instrucciones
print("\n\nSi en el turno 1 sale un\n7 u 11, ganas!\n2, 3 o 12, pierdes!\nOtro número, se guarda como punto y se tiran otra vez los dados\n")
print("Del turno 2 en adelante\nTu punto, ganas!\n7 pierdes!\n\n")
print("\tEmpieza el juego\n")

#Mientras la opción sea 1, se da la opción de juegar otra vez
while op == 1:
    op = int(input("¿Tirar dados?\n1.Sí\n2.No\nOpción: "))
    #Si la opción es 1, empieza el juego
    if op ==1:
        #Se borra la pantalla entre juegos
        os.system ("cls")
        #Se tiran los dados por primera vez
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        suma = dado1 + dado2
        #Se guarda la suma en el punto por si es un número distinto a los ganadores o perdedores
        punto = suma
        turno = 1
        #Si en el primer tiro la suma de los dados es 7 u 11, se gana
        if (suma == 7 or suma == 11):
            print("\n\nJuego número " + str(juego))
            print("\n\nTurno 1")
            print("Tus números son: " + str(dado1) + " + " + str(dado2) + " = " + str(suma))
            print("Ganaste :)\n\n")
        #Si en el primer tiro la suma de los dados es 2, 3 o 12, se pierde
        elif (suma == 2 or suma == 3 or suma == 12):
            print("\n\nJuego número " + str(juego))
            print("\n\nTurno 1")
            print("Tus números son: " + str(dado1) + " + " + str(dado2) + " = " + str(suma))
            print("Perdiste :(\n\n")
        #Si en el primer tiro la suma de los dados es cualquier otro número, se guarda en punto y se vuele a tirar
        else:
            print("\n\nJuego número " + str(juego))
            print("\n\nTurno 1")
            print("Tus números son: " + str(dado1) + " + " + str(dado2) + " = " + str(suma))
            print("Por lo que tu punto es: " + str(punto))
            print("Se vuelven a tirar los dados...")
            #Mientras la suma no sea 7 o el punto, se ejecuta el while
            while suma != 7:
                #Se tiran los dados 
                dado1 = random.randint(1,6)
                dado2 = random.randint(1,6)
                suma = dado1 + dado2
                turno += 1
                if suma == punto:
                    print("\n\nTurno " + str(turno))
                    print("Tus números son: " + str(dado1) + " + " + str(dado2) + " = " + str(suma))
                    print("El resultado es igual que tu punto: " + str(punto))
                    print("Ganaste :)\n\n")
                    suma = 7
                elif suma == 7:
                    print("\n\nTurno " + str(turno))
                    print("Tus números son: " + str(dado1) + " + " + str(dado2) + " = " + str(suma))
                    print("Perdiste :(, tu resultado fue: " + str(suma) + "\n\n")
                else:
                    print("\n\nTurno " + str(turno))
                    print("Tus números son: " + str(dado1) + " + " + str(dado2) + " = " + str(suma))
                    print("Se vuelven a tirar los dados...")
    #Si la opción es 2 o cualquier otro número, se sale del juego
    else:
        op = 2
    #Incrementa el número de juegos en 1
    juego += 1
#Se borra toda la pantalla
os.system ("cls")
print("\nSaliste del juego\n")