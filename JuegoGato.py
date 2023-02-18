#Juego de gato / tic tac toe
#Sánchez Medina Paola Guadalupe

#Como jugar
print("\t\t\t\t~~~~~~JUEGO DE GATO~~~~~~")
print("\t\t\t\t~~~~~~TIC TAC TOE~~~~~~~~\n\n")

print("El primer jugador en completar 3 casillas seguidas con \"X\" o con \"O\", en vertical, horizontal o diagonal, GANA! :D")
print("Dos jugadores se enfrentan, tira uno y después el otro.")
print("Ejemplo...\n\n")

print("\t   |   |              X | O | O ")
print("\t-----------          -----------")
print("\t   |   |      --->      | X | O ")
print("\t-----------          -----------")
print("\t   |   |                |   | X \n\n")

print("La X gana!!!\n\n\n")

#Código
# 2 = vacío, 3 = X, 5 = O 
#Se importa la libreria random, para la función make2
import random

#variables globales
gato = [2,2,2,2,2,2,2,2,2]
turno = 1
gana = False
aux = gana

#Funciones

#Imprime el gato con el número de las casillas, no se actualiza con los movimientos
def muestraGato():
    print("\t\t\t   1 | 2 | 3")
    print("\t\t\t  -----------")
    print("\t\t\t   4 | 5 | 6")
    print("\t\t\t  -----------")
    print("\t\t\t   7 | 8 | 9")

#Iprime el gato, se actualiza con los movimientos
def imprimeGato(casillasGato):
    #Cambia los números por caracteres
    for x in range(len(casillasGato)):
        if casillasGato[x] == 2:
            casillasGato[x] = " "
        elif casillasGato[x] == 3:
            casillasGato[x] = "X"
        elif casillasGato[x] == 5:
            casillasGato[x] = "O"

    print("\t\t\t   " + casillasGato[0] + " | "+ casillasGato[1] + " | " + casillasGato[2] + "\t\t\t   1 | 2 | 3")
    print("\t\t\t  -----------" + "\t\t\t  -----------")
    print("\t\t\t   " + casillasGato[3] + " | "+ casillasGato[4] + " | " + casillasGato[5] + "\t\t\t   4 | 5 | 6")
    print("\t\t\t  -----------" + "\t\t\t  -----------")
    print("\t\t\t   " + casillasGato[6] + " | "+ casillasGato[7] + " | " + casillasGato[8] + "\t\t\t   7 | 8 | 9")

    #Cambia los caracteres por números
    for x in range(len(casillasGato)):
        if casillasGato[x] == " ":
            casillasGato[x] = 2
        elif casillasGato[x] == "X":
            casillasGato[x] = 3
        elif casillasGato[x] == "O":
            casillasGato[x] = 5

#Verifica si la PC gana 5 * 5 * 5 = 125
def verificaGana(verifica):
    #Fila de arriba 0 1 2
    if ((verifica[0] * verifica[1] * verifica[2]) == 125):
        return True
    #Fila de en medio 3 4 5
    elif ((verifica[3] * verifica[4] * verifica[5]) == 125):
        return True
    #Fila de abajo 6 7 8
    elif ((verifica[6] * verifica[7] * verifica[8]) == 125):
        return True
    #Columna 1 0 3 6
    elif ((verifica[0] * verifica[3] * verifica[6]) == 125):
        return True
    #Columna 2 1 4 7
    elif ((verifica[1] * verifica[4] * verifica[7]) == 125):
        return True
    #Columna 3 2 5 8
    elif ((verifica[2] * verifica[5] * verifica[8]) == 125):
        return True
    #Diagonal 0 4 8
    elif ((verifica[0] * verifica[4] * verifica[8]) == 125):
        return True
    #Diagonal invertida 2 4 6
    elif ((verifica[2] * verifica[4] * verifica[6]) == 125):
        return True
    else:
        return False

#Posiciones del gato, [0,1,2, 3,4,5, 6,7,8]
#Verifica si la siguiente jugada del jugador es la ganadora, si sí, entomces pone una O en la posición ganadora
#Verifica si la siguiente jugada de la PC es la ganadora, si sí, entomces pone una O en la posición ganadora
def possWin(valida, vTurno):
    #Fila de arriba 0 1 2
    if ((valida[0] * valida[1] * valida[2]) == 18):
        if valida[0] == 2:
            valida[0] = 5
            imprimeGato(valida)
        elif valida[1] == 2:
            valida[1] = 5
            imprimeGato(valida)
        elif valida[2] == 2:
            valida[2] = 5
            imprimeGato(valida)
    #Fila de en medio 3 4 5
    elif ((valida[3] * valida[4] * valida[5]) == 18):
        if valida[3] == 2:
            valida[3] = 5
            imprimeGato(valida)
        elif valida[4] == 2:
            valida[4] = 5
            imprimeGato(valida)
        elif valida[5] == 2:
            valida[5] = 5
            imprimeGato(valida)
    #Fila de abajo 6 7 8
    elif ((valida[6] * valida[7] * valida[8]) == 18):
        if valida[6] == 2:
            valida[6] = 5
            imprimeGato(valida)
        elif valida[7] == 2:
            valida[7] = 5
            imprimeGato(valida)
        elif valida[8] == 2:
            valida[8] = 5
            imprimeGato(valida)
    #Columna 1 0 3 6
    elif ((valida[0] * valida[3] * valida[6]) == 18):
        if valida[0] == 2:
            valida[0] = 5
            imprimeGato(valida)
        elif valida[3] == 2:
            valida[3] = 5
            imprimeGato(valida)
        elif valida[6] == 2:
            valida[6] = 5
            imprimeGato(valida)
    #Columna 2 1 4 7
    elif ((valida[1] * valida[4] * valida[7]) == 18):
        if valida[1] == 2:
            valida[1] = 5
            imprimeGato(valida)
        elif valida[4] == 2:
            valida[4] = 5
            imprimeGato(valida)
        elif valida[7] == 2:
            valida[7] = 5
            imprimeGato(valida)
    #Columna 3 2 5 8
    elif ((valida[2] * valida[5] * valida[8]) == 18):
        if valida[2] == 2:
            valida[2] = 5
            imprimeGato(valida)
        elif valida[5] == 2:
            valida[5] = 5
            imprimeGato(valida)
        elif valida[8] == 2:
            valida[8] = 5
            imprimeGato(valida)
    #Diagonal 0 4 8
    elif ((valida[0] * valida[4] * valida[8]) == 18):
        if valida[0] == 2:
            valida[0] = 5
            imprimeGato(valida)
        elif valida[4] == 2:
            valida[4] = 5
            imprimeGato(valida)
        elif valida[8] == 2:
            valida[8] = 5
            imprimeGato(valida)
    #Diagonal invertida 2 4 6
    elif ((valida[2] * valida[4] * valida[6]) == 18):
        if valida[2] == 2:
            valida[2] = 5
            imprimeGato(valida)
        elif valida[4] == 2:
            valida[4] = 5
            imprimeGato(valida)
        elif valida[6] == 2:
            valida[6] = 5
            imprimeGato(valida)
    #Verifica movimiento ganador de la PC
    elif ((valida[0] * valida[1] * valida[2]) == 50):
        if valida[0] == 2:
            valida[0] = 5
            imprimeGato(valida)
        elif valida[1] == 2:
            valida[1] = 5
            imprimeGato(valida)
        elif valida[2] == 2:
            valida[2] = 5
            imprimeGato(valida)
    #Fila de en medio 3 4 5
    elif ((valida[3] * valida[4] * valida[5]) == 50):
        if valida[3] == 2:
            valida[3] = 5
            imprimeGato(valida)
        elif valida[4] == 2:
            valida[4] = 5
            imprimeGato(valida)
        elif valida[5] == 2:
            valida[5] = 5
            imprimeGato(valida)
    #Fila de abajo 6 7 8
    elif ((valida[6] * valida[7] * valida[8]) == 50):
        if valida[6] == 2:
            valida[6] = 5
            imprimeGato(valida)
        elif valida[7] == 2:
            valida[7] = 5
            imprimeGato(valida)
        elif valida[8] == 2:
            valida[8] = 5
            imprimeGato(valida)
    #Columna 1 0 3 6
    elif ((valida[0] * valida[3] * valida[6]) == 50):
        if valida[0] == 2:
            valida[0] = 5
            imprimeGato(valida)
        elif valida[3] == 2:
            valida[3] = 5
            imprimeGato(valida)
        elif valida[6] == 2:
            valida[6] = 5
            imprimeGato(valida)
    #Columna 2 1 4 7
    elif ((valida[1] * valida[4] * valida[7]) == 50):
        if valida[1] == 2:
            valida[1] = 5
            imprimeGato(valida)
        elif valida[4] == 2:
            valida[4] = 5
            imprimeGato(valida)
        elif valida[7] == 2:
            valida[7] = 5
            imprimeGato(valida)
    #Columna 3 2 5 8
    elif ((valida[2] * valida[5] * valida[8]) == 50):
        if valida[2] == 2:
            valida[2] = 5
            imprimeGato(valida)
        elif valida[5] == 2:
            valida[5] = 5
            imprimeGato(valida)
        elif valida[8] == 2:
            valida[8] = 5
            imprimeGato(valida)
    #Diagonal 0 4 8
    elif ((valida[0] * valida[4] * valida[8]) == 50):
        if valida[0] == 2:
            valida[0] = 5
            imprimeGato(valida)
        elif valida[4] == 2:
            valida[4] = 5
            imprimeGato(valida)
        elif valida[8] == 2:
            valida[8] = 5
            imprimeGato(valida)
    #Diagonal invertida 2 4 6
    elif ((valida[2] * valida[4] * valida[6]) == 50):
        if valida[2] == 2:
            valida[2] = 5
            imprimeGato(valida)
        elif valida[4] == 2:
            valida[4] = 5
            imprimeGato(valida)
        elif valida[6] == 2:
            valida[6] = 5
            imprimeGato(valida)
    else:
        make2(valida, vTurno)
#gato [0,1,2, 
#      3,4,5, 
#      6,7,8]
#Función que sale de trampa
def make2(trampa, nTurno):
    #Centro
    if trampa[4] == 2:
        trampa[4] = 5
        imprimeGato(trampa)
    #Sale de la trampa de dos X en centros juntos
    elif trampa[1] == 3 and trampa[5] == 3:
        trampa[2] = 5
        imprimeGato(trampa)
    elif trampa[1] == 3 and trampa[3] == 3:
        trampa[0] = 5
        imprimeGato(trampa)
    elif trampa[3] == 3 and trampa[7] == 3:
        trampa[6] = 5
        imprimeGato(trampa)
    elif trampa[5] == 3 and trampa[7] == 3:
        trampa[8] = 5
        imprimeGato(trampa)
        #Noncorner
    elif trampa[1] == 2:
        trampa[1] = 5
        imprimeGato(trampa)
    elif trampa[3] == 2:
        trampa[3] = 5
        imprimeGato(trampa)
    elif trampa[5] == 2:
        trampa[5] = 5
        imprimeGato(trampa)
    elif trampa[7] == 2:
        trampa[7] = 5
        imprimeGato(trampa)
    elif (nTurno == 2 or nTurno == 4 or nTurno == 6 or nTurno == 8):
        if trampa[0] == 2:
            trampa[0] = 5
            imprimeGato(trampa)
        elif trampa[2] == 2:
            trampa[2] = 5
            imprimeGato(trampa)
        elif trampa[6] == 2:
            trampa[6] = 5
            imprimeGato(trampa)
        elif trampa[8] == 2:
            trampa[8] = 5
            imprimeGato(trampa)
    else:
        go(trampa)

#Hace un movimiento random en una casilla vacía
def go(movGato):
        numero = random.randint(0,8)
        if movGato[numero] == 2:
            movGato[numero] = 5
            imprimeGato(movGato)
        else:
            go(movGato)

#Main
print("\t\t\tINICIO DEL JUEGO\n\n")
print("Se muestran los números de las casillas del gato:\n")
muestraGato()

print("\n\nEres las X, la PC es las O")
print("¿Te gustaría empezar? elige un número :) \n 1.Sí\n 2.No")
op = int(input("Opción: "))

if op == 1:
    #Empieza el jugador
    print("Turno 1, empieza el jugador")
    casilla = int(input("Ingresa el número de la casilla que vas a jugar: "))
    casilla -= 1
    gato[casilla] = 3
    imprimeGato(gato)
    #Mientras nadie haya ganado se repiten las jugadas
    while turno <= 9 and gana == False:
        aux = verificaGana(gato)
        gana = aux
        turno += 1
        #Si aún hay espacios, se hace la siguiente jugada
        if gana == False and turno <= 9:
            #Tira la PC
            print("\nTurno " + str(turno) + " de la PC")
            possWin(gato, turno)
            aux = verificaGana(gato)
            gana = aux
            turno += 1
            #Si aún hay espacios, se hace la siguiente jugada
            if gana == False and turno <= 9:
                #Tira el jugador
                print("\nTurno " + str(turno) + " del jugador")
                casilla = int(input("Ingresa el número de la casilla que vas a jugar: "))
                casilla -= 1
                gato[casilla] = 3
                imprimeGato(gato)
                aux = verificaGana(gato)
                gana = aux
    print("Fin del juego")
elif op == 2:
    #Empieza la PC
    print("Turno 1, empieza la PC")
    possWin(gato, turno)
    #Mientras nadie haya ganado se repiten las jugadas
    while turno <= 9 and gana == False:
        turno += 1
        aux = verificaGana(gato)
        gana = aux
        #Si aún hay espacios, se hace la siguiente jugada
        if gana == False and turno <= 9:
            #Tira el jugador
            print("\nTurno " + str(turno) + " del jugador")
            casilla = int(input("Ingresa el número de la casilla que vas a jugar: "))
            casilla -= 1
            gato[casilla] = 3
            imprimeGato(gato)
            aux = verificaGana(gato)
            gana = aux
            turno += 1
            #Si aún hay espacios, se hace la siguiente jugada
            if gana == False and turno <= 9:
                #Tira PC
                print("\nTurno " + str(turno) + " de la PC")
                possWin(gato, turno)
                aux = verificaGana(gato)
                gana = aux
    print("Fin del juego")
else:
    print("Opción incorrecta")