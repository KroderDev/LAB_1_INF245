import random

def convertir_a_decimal(num, base):
    try:
        match base:
            case 'BIN':
                decimal = 0
                power = 0
                for i in reversed(str(num)):
                    if i == '1': # Si el bit es 1 sumamos 2**(portencia) al decimal
                        decimal += 2**power
                    elif i != '0': # Manejo de error
                        raise('El número binario es inválido.')

                    power+=1 # incrementar la potencia
                return decimal
            case 'OCT':
                pass
            case 'HEX':
                pass
            case _:
                return None
    except:
        raise ValueError('Ocurrió un error inesperado')

class Tablero:
    """Tablero"""
    def __init__(self, largo, guardias):
        self.largo = largo
        self.guardias = guardias
        self.tablero = [['░' for _ in range(largo)] for _ in range(11)]
        self.snake_pos = (5, 0)  # Posicion Snake
        self.objetivo_pos = None
        self.generar_tablero()

    def generar_tablero(self):
        """Genera el tablero inicial con Snake, objetivo y guardias."""
        # Colocar Snake
        self.tablero[self.snake_pos[0]][self.snake_pos[1]] = 'S'

        # Colocar Objetivo
        objetivo_row = random.randint(0, 10)
        self.objetivo_pos = (objetivo_row, self.largo - 1)
        self.tablero[objetivo_row][self.largo - 1] = '*'

        # Colocar Guardias
        for _ in range(self.guardias):
            while True:
                row = random.randint(0, 10)
                col = random.randint(0, self.largo - 2)
                if self.tablero[row][col] == '░':
                    self.tablero[row][col] = '!'
                    break

    def mover_snake(self, direccion, pasos):
        """Mueve al jugador."""
        fila, col = self.snake_pos
        self.tablero[fila][col] = '░'  # Limpia la posición anterior

        for _ in range(pasos):
            if direccion == 'w' and fila > 0:
                fila -= 1
            elif direccion == 's' and fila < 10:
                fila += 1
            elif direccion == 'a' and col > 0:
                col -= 1
            elif direccion == 'd' and col < self.largo - 1:
                col += 1
            else:
                break  # Evita moverse fuera del tablero

        self.snake_pos = (fila, col)
        self.tablero[fila][col] = 'S'

    def mostrar(self):
        for row in self.tablero:
            print(' '.join(row))
        print()

def main():
    """Función main"""
    print("Bienvenido a METAL GEAR SOLID 1010: BINARY SNAKE")
    largo = int(input("Ingrese el largo del pasillo: "))
    guardias = int(input("Ingrese la cantidad de guardias: "))
    tablero = Tablero(largo, guardias)

    while True:
        tablero.mostrar()
        print("Ingresa una acción:")
        print("w: moverse hacia arriba")
        print("s: moverse hacia abajo")
        print("a: moverse a la izquierda")
        print("d: moverse a la derecha")
        print("-1: salir")
        mov = input("Dirección: ")
        if mov == "-1":
            break
        pasos = int(input("Cantidad de pasos: "))
        tablero.mover_snake(mov, pasos)

main()
