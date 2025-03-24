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
                col = random.randint(0, self.largo - 2)  # (sin tocar la columna final)
                if self.tablero[row][col] == '░':
                    self.tablero[row][col] = '!'
                    break

    def mostrar(self):
        for row in self.tablero:
            print(' '.join(row))
        print()

def main():
    print("Bienvenido a METAL GEAR SOLID 1010: BINARY SNAKE")
    largo = int(input("Ingrese el largo del pasillo: "))
    guardias = int(input("Ingrese la cantidad de guardias: "))
    
    tablero = Tablero(largo, guardias)
    tablero.mostrar()

main()