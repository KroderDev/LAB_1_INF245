# METAL GEAR SOLID 1010: BINARY SNAKE

## Documentación

### Función: `convertir_a_decimal`
Convierte a decimal el número ingresado de base indicada aplicando algorítmos de conversión.
#### **Parámetros**
- num (`int` o `str`): Número a convertir.
- **base** (`str`): Clave de la base numérica en el diccionario `bases`. Debe ser una de las siguientes:
  - `'BIN'` para números binarios.
  - `'OCT'` para números octales.
  - `'HEX'` para números hexadecimales.
#### **Retorna**
- `int`: El número de entrada convertido a decimal.

### Diccionario: `bases`

Contiene la información para validar y convertir números en diferentes bases.

- **`BIN`**
  - **key:** `'BIN'`
  - **name:** `'Binario'`
  - **regex:** `r'^[01]+$'` (dígitos 0 y 1)

- **`OCT`**
  - **key:** `'OCT'`
  - **name:** `'Octal'`
  - **regex:** `r'^[0-7]+$'` (dígitos del 0 al 7)

- **`HEX`**
  - **key:** `'HEX'`
  - **name:** `'Hexadecimal'`
  - **regex:** `r'^[0-9A-Fa-f]+$'` (dígitos 0-9 y letras A-F)


### Clase: `Tablero`

## Contacto
* **Sebastián Richiardi**, Rol; 20203055-2, Paralelo: 201
* **Gabriel Alejandro Toro Varela**, Rol; 202204557-4, Paralelo: 201
