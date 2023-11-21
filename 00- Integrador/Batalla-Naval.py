from random import randint

# Funcion para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
        
# Funcion para colocar los barcos en el tablero
def colocar_barcos(tablero, num_barcos):
    for _ in range(num_barcos):
        fila = randint(0, len(tablero) - 1)
        columna = randint(0, len(tablero[0]) - 1)
        
        while tablero[fila][columna] == "X":
            fila = randint(0, len(tablero) - 1)
            columna = randint(0, len(tablero[0]) - 1)
            
        tablero[fila][columna] = "X"
        
# Funcion para atacar
def atacar(tablero, fila, columna):
    if tablero[fila][columna] == "X":
        print("Has golpeado un barco!")
        # Marcar como hundido
        tablero[fila][columna] = "H"
        return True
    else:
        print("Agua. Intenta nuevamente.")
        return False

# Configuracion del juego
filas = 5
columnas = 5
num_barcos = 3

# Inicializar tablero
tablero = [["O" for _ in range(columnas)] for _ in range(filas)]

# Colocar barcos
colocar_barcos(tablero, num_barcos)

# Juego
intentos = 0

while True:
    print(f"\nIntento #{intentos + 1}")
    imprimir_tablero(tablero)
    
    try:
        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))
    except ValueError:
        print("Ingrese números válidos.")
        continue
    
    if 0 <= fila < filas and 0 <= columna < columnas:
        if atacar(tablero, fila, columna):
            intentos += 1
            barcos_restantes = sum(fila.count("X") for fila in tablero)
            if barcos_restantes == 0:
                imprimir_tablero(tablero)
                print(f"¡Ganaste! Todos los barcos fueron destruidos en {intentos} intentos.")
                break
        else:
            intentos += 1
    else:
        print("Coordenadas fuera de rango. Inténtalo de nuevo.")