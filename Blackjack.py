import random

mazo = []
jugadores = []
experimentar = []
def generar_mazos(n):
    global mazo
    if n>0:
        for i in range(n):

            mazo= mazo + [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2,
                           3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            random.shuffle(mazo)

        print ("el total de cartas es de: " + str(len(mazo)))
        return mazo
    else:
        return 0

def jugar(m):
    if (len(m)>0):
        a = 0
        while (a < 21):
            a += mazo.pop(0)
            #print (a)
            if (a == 21):
                return a

            elif (a > 21):
                return a
    else:
        return 0
def jugar_varios(m, j):
    global jugadores
    for i in range(j):
        jugadores.insert(i,jugar(m))
    return mazo
def ver_quien_gano(j):
    global jugadores
    for i in range(len(jugadores)):
        if jugadores[i] == 21:
            print ("el jugador " + str(i+1) + " gano con " + str(jugadores[i]) + " pts.")
        else:
            print ("el jugador " + str(i+1) + " no gano, saco " + str(jugadores[i]) + " pts.")
def ver_cartas_finales():
    print (len(mazo))
    return len(mazo)
def experimentar (rep,n):
    for i in range (rep):
        for j in range (n):
            jugadores.insert(i, jugar(m))
            if jugadores[i]==21
        return mazo
    return


generar_mazos(4)
jugar_varios(mazo,4)
ver_quien_gano(jugadores)
ver_cartas_finales()