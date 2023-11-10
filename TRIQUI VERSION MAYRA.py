
#triqui version: Mayra

import random # es para generar numeros aleatorios
 
tablero = [[" " for _ in range(3)] for _ in range(3)]  # inicia con los espacios en blancos con tres espacios
jugadores = ["X", "O"]  #lista de jugadores
juego_terminado = False  # Variable para controlar el estado del juego y tambien para ver si el juag ha terinado

# impresion del tablero
def imprimir_tablero():
    for fila in tablero:
        print("|".join(fila))
        print("-+-+-")


def verificar_ganador(jugador): # nombre de la funcion, verifica si un jugador ha ganado
    for fila in tablero: #representa cada fila del tablero
     if fila.count(jugador) == 3: #verifica si el jugandor a completado una fila
           return True #devuelve un valor indica que se ha encontrado un ganador

    #verificacion de las columnas        
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador: #verifica si el jugador esta en tres posiciones 
            return True #indica que el juego ha terminado y se ha encontrado un jugador
    
    # Verificacion de las diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador: #es para ver que el jugadro ha completado la diagonal y ha ganado
        return True #para ver que se ha encontrado un ganador
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    
    return False


def hay_empate(): # Función para determinar si hay empate
    for fila in tablero:
        if " " in fila:
            return False
    return True

def movimiento_maquina():# esto hace que la maquina realice un moviemiento
    disponibles = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    return random.choice(disponibles)


def jugar_triki(): #funcion del juego principal
    global juego_terminado

    while not juego_terminado: #esto imprime el tablero
        imprimir_tablero() 

        #turno de los jugadores
        fila = int(input("Ingrese el número de fila (0-2): "))
        columna = int(input("Ingrese el número de columna (0-2): "))  
        
        # Validar la entrada del usuario
        if 0 <= fila <= 2 and 0 <= columna <= 2 and tablero[fila][columna] == " ":
            tablero[fila][columna] = jugadores[0]
            
            # Verificar si el usuario ganó
            if verificar_ganador(jugadores[0]):
                imprimir_tablero()
                print("fELICIDADES, HAS GANADO")
                juego_terminado = True
                break
            elif hay_empate():
                imprimir_tablero()
                print("EMPATE")
                juego_terminado = True
                break
        else:
            print("MOVIMIENTO NO VALIDO, INTENTA NUEVAMENTE")
            continue
        
        # Turno de la máquina
        print("Turno de la máquina:")
        fila_maquina, columna_maquina = movimiento_maquina()
        tablero[fila_maquina][columna_maquina] = jugadores[1]
        
        # Verificar si la máquina ganó
        if verificar_ganador(jugadores[1]):
            imprimir_tablero()
            print("EL COMPUTADRO HA GANADO... SUERTE PARA LA PROXIMA")
            juego_terminado = True
            break
        elif hay_empate():
            imprimir_tablero()
            print("ES OTRO EMPATE")
            juego_terminado = True
            break

# Menú para seguir o salir del juego
while True:
    jugar_triki()
    opcion = input(" QUIERES SEGUIR? (si/no): ")
    if opcion.lower() != 'si':
        break
    else:
        #Reinicia todo para jugar nuevamente
        tablero = [[" " for _ in range(3)] for _ in range(3)]
        juego_terminado = False 