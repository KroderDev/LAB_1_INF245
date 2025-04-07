import random
import re
import time

# Diccionario para las direcciones
directions = {
    'w': 'Arriba',
    's': 'Abajo',
    'a': 'Izquierda',
    'd': 'Derecha'
}

# Dicccionario para las bases
bases = {
    'BIN': {'key':'BIN', 'name':'Binario', 'regex':r'^[01]+$'},
    'OCT': {'key':'OCT', 'name':'Octal', 'regex':r'^[0-7]+$'},
    'HEX': {'key':'HEX', 'name':'Hexadecimal', 'regex':r'^[0-9A-Fa-f]+$'}
}

class Tablero:
    """Tablero"""
    def __init__(self, largo: int, guardias: int):
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

    def mover_snake(self, direccion: str, pasos: int):
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

def convertir_a_decimal(num: str, base: str) -> int:
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
                return int(decimal)
            case 'OCT':
                decimal = 0
                power = 0

                # Recorrer dígitos de derecha a izquierda
                for i in reversed(str(num)):
                    decimal += int(i) * (8 ** power)
                    power += 1

                return int(decimal)
            case 'HEX':
                decimal = 0
                power = 0
                hex_digits = '0123456789ABCDEF'

                for i in reversed(str(num).upper()):  # Trabajamos con mayúsculas
                    if i not in hex_digits:
                        raise ValueError('El número hexadecimal es inválido.')
                    decimal += hex_digits.index(i) * (16 ** power)
                    power += 1

                return int(decimal)
            case _:
                return 0
    except:
        raise ValueError('Ocurrió un error inesperado')
    
def convertir_a_binario(num: int) -> str:
    if num == 0:
        return '0'
    binario = ''
    while num > 0:
        binario = str(num % 2) + binario
        num //= 2
    return binario

def convertir_a_octal(num: int) -> str:
    if num == 0:
        return '0'
    octal = ''
    while num > 0:
        octal = str(num % 8) + octal
        num //= 8
    return octal

def convertir_a_hexadecimal(num: int) -> str:
    if num == 0:
        return '0'
    hex_digits = '0123456789ABCDEF'
    hexadecimal = ''
    while num > 0:
        hexadecimal = hex_digits[num % 16] + hexadecimal
        num //= 16
    return hexadecimal

def iniciar_hackeo(tablero: Tablero, base: str):
    # Iniciamos el hackeo
    print("Iniciando hackeo", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.25)

    print("\n" * 5)

    # Mostramos una barra de progreso
    for _ in range(100):
        print("█", end="", flush=True)
        time.sleep(0.005)
    time.sleep(.25)
    print("")
    
    # Generamos una clave de hackeo aleatoria
    if base == 'BIN':
        clave_hackeo = convertir_a_binario(random.randint(0, 20))
    elif base == 'OCT':
        clave_hackeo = convertir_a_octal(random.randint(0, 100))
    elif base == 'HEX':
        clave_hackeo = convertir_a_hexadecimal(random.randint(0, 500))

    print(f"La clave encriptada es: {clave_hackeo}")
    time.sleep(.25)
    print("")

    # Solicitamos la clave de acceso al usuario
    while True:
        try:
            input_usuario = int(input("Introduce la clave de acceso: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

    # Mostramos una barra de progreso
    for i in range(100):
        print("█", end="", flush=True)
        time.sleep(.05 * random.uniform(.5, 1.5))
    time.sleep(.5)
    print("")

    # Verificamos si la clave es correcta
    if base == 'BIN':
        clave_correcta = clave_hackeo == convertir_a_binario(input_usuario)
    elif base == 'OCT':
        clave_correcta = clave_hackeo == convertir_a_octal(input_usuario)
    elif base == 'HEX':
        clave_correcta = clave_hackeo == convertir_a_hexadecimal(input_usuario)

    # Mostramos el resultado del hackeo
    if clave_correcta == True:
        print("Hackeo exitoso. Acceso concedido.") 
        victoria(tablero) # Si el hackeo es exitoso, se llama a la funcion de victoria
    else:
        print("Hackeo fallido. Acceso denegado.")
        derrota(tablero) # Si el hackeo falla, se llama a la funcion de derrota

def victoria(tablero: Tablero):
    print(r"""
███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗
██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗
╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║
███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║
╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝
""")
    print("¡MISIÓN CUMPLIDA! Te has infiltrado con éxito.")
    exit(0)

def derrota(tablero: Tablero):
    print(r"""
███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
█████╗  ███████║██║██║     █████╗  ██║  ██║
██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
██║     ██║  ██║██║███████╗███████╗██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
""")
    print("¡ALERTA! Snake fue detectado. Fin de la misión.")
    exit(0)

def convertir_a_decimal2(num, base): #hice mi propia version de la funcion xd, no se que te parece
    """Convierte un número de base BIN, OCT o HEX a decimal manualmente."""
    # Definir bien las bases
    bases_validas = {
        'BIN': ('01', 2),
        'OCT': ('01234567', 8),
        'HEX': ('0123456789ABCDEF', 16)}

    base = str(base).upper()
    if base not in bases_validas:
        return f"Base {base} no existe."


    caracteres_validos, base_num = bases_validas[base]
    decimal = 0
    potencia = 0

    # Convertir el número a mayúsculas para manejar HEX correctamente
    num = str(num).upper()

    # Recorrer el número de derecha a izquierda
    for digito in reversed(num):
        if digito not in caracteres_validos:
            return f"El número {num} no es válido en base {base}."

        valor = caracteres_validos.index(digito)  # Obtener su valor en la base
        decimal += valor * (base_num ** potencia)
        potencia += 1

    return decimal

def main():
    """Función main"""
    print("Bienvenido a METAL GEAR SOLID 1010: BINARY SNAKE")

    # Solicitar el largo del pasillo
    while True:
        try:
            largo = int(input("Ingrese el largo del pasillo: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            
    # Solicitar la cantidad de guardias
    while True:
        try:
            guardias = int(input("Ingrese la cantidad de guardias: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    # Crear el tablero
    tablero = Tablero(largo, guardias)

    # SET BASE
    if largo <= 20:
        base = bases['BIN']
    elif largo <= 100:
        base = bases['OCT']
    else:
        base = bases['HEX']

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
        if mov not in directions:
            print("Dirección inválida. Intenta de nuevo.")
            continue

        # Solicitar y validar entrada para la base
        while True:
            num_input = input("Escribe la cantidad de pasos que quieres moverte hacia %s en formato %s: " % (directions[mov], base['name']))
            if re.fullmatch(base['regex'], num_input):
                break
            else:
                print("El valor ingresado no es válido para la base %s. Intenta de nuevo." % base['name'])

        pasos = convertir_a_decimal(num_input, base['key'])
        tablero.mover_snake(mov, pasos)
        if tablero.snake_pos == tablero.objetivo_pos:
            iniciar_hackeo(tablero, base['key'])
            break

if __name__ == "__main__":
    main()
    
