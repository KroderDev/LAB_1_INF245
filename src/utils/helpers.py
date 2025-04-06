import os
import time
import random
from src.models.tablero import Tablero
from src.utils.converters import convertir_a_binario, convertir_a_octal, convertir_a_hexadecimal, convertir_a_decimal

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

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def iniciar_hackeo(tablero: Tablero, base: str):
    limpiar_pantalla()
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
    time.sleep(.5)
    limpiar_pantalla()
    
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
        time.sleep(.025 * random.uniform(.5, 1.5))
    time.sleep(.5)
    print("")

    # Verificamos si la clave es correcta
    if base == 'BIN':
        clave_correcta = clave_hackeo == convertir_a_binario(input_usuario)
    elif base == 'OCT':
        clave_correcta = clave_hackeo == convertir_a_octal(input_usuario)
    elif base == 'HEX':
        clave_correcta = clave_hackeo == convertir_a_hexadecimal(input_usuario)

    limpiar_pantalla()
    print("\n" * 5)
    # Mostramos el resultado del hackeo
    if clave_correcta == True:
        print("Hackeo exitoso. Acceso concedido.") 
        victoria(tablero) # Si el hackeo es exitoso, se llama a la funcion de victoria
    else:
        print("Hackeo fallido. Acceso denegado.")
        derrota(tablero) # Si el hackeo falla, se llama a la funcion de derrota