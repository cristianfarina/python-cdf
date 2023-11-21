from random import randint

# Constantes para los jugadores
JUGADOR_O = "O"
JUGADOR_X = "X"

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def obtener_jugador(jugadores):
    while True:
        try:
            indice = int(input("Ingrese el número de jugador: 0 para 'O' ; 1 para 'X' "))
            
            if indice == 0 or indice == 1:
                jugador_elegido = jugadores[indice]
                return jugador_elegido
            else:
                print("Por favor, ingrese valores válidos para el número de jugador.")
        except ValueError:
            print("Por favor, ingrese valores numéricos.")

def obtener_movimiento_jugador(jugador):
    while True:
        try:
            fila = int(input(f"Ingrese el número de fila (0, 1, 2) para el jugador {jugador}: "))
            columna = int(input(f"Ingrese el número de columna (0, 1, 2) para el jugador {jugador}: "))

            if 0 <= fila < 3 and 0 <= columna < 3:
                return fila, columna
            else:
                print("Por favor, ingrese valores válidos para la fila y la columna.")
        except ValueError:
            print("Por favor, ingrese valores numéricos.")


def jugar_tateti():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = [JUGADOR_O, JUGADOR_X]
    turno = 0
    jugador_elegido = obtener_jugador(jugadores)
    
    if jugador_elegido == jugadores[0]:
        jugador_maquina = jugadores[1]
    else:
        jugador_maquina = jugadores[0]
        
    while True:
        imprimir_tablero(tablero)
        jugador_actual = jugadores[turno % 2]
        print(f"Turno del jugador {jugador_actual}")

        if jugador_actual == jugador_maquina:
            fila = randint(0,2)
            columna = randint(0,2)             
        else:
            fila, columna = obtener_movimiento_jugador(jugador_actual)

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡El jugador {jugador_actual} ha ganado!")
                break
            elif all(tablero[i][j] != " " for i in range(3) for j in range(3)):
                imprimir_tablero(tablero)
                print("¡Empate!")
                break
            else:
                turno += 1
        else:
            print("La posición ya está ocupada. Inténtelo de nuevo.")
            if jugador_actual == jugador_maquina:
                fila = randint(0,2)
                columna = randint(0,2) 
  
jugar_tateti()
