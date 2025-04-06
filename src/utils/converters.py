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
