import random
import re
import time
from src.models.tablero import Tablero
from src.utils.converters import convertir_a_binario, convertir_a_octal, convertir_a_hexadecimal, convertir_a_decimal
from src.utils.helpers import directions, bases, victoria, derrota, limpiar_pantalla
from src.utils.helpers import iniciar_hackeo

def main():
    """Función main"""
    print("Bienvenido a METAL GEAR SOLID 1010: BINARY SNAKE")
    
    print("\n" * 5)

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

    # Iniciando juego
    print("Cargando", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.25)

    while True:
        limpiar_pantalla()
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

if __name__ == "__main__":
    limpiar_pantalla()
    main()
    tablero = Tablero(10, 5)
    iniciar_hackeo(tablero, 'BIN')
    
