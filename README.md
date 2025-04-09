# METAL GEAR SOLID 1010: BINARY SNAKE

## Documentación

### Función: `convertir_a_decimal`
Convierte a decimal el número ingresado de base indicada aplicando algorítmos de conversión. Para la conversión usaremos algorítmos basados en poténcias, como si se hiciera el cálculo a mano.
#### **Parámetros**
- num (`str`): Número a convertir.
- **base** (`str`): Clave de la base numérica en el diccionario `bases`. Debe ser una de las siguientes:
  - `'BIN'` para números binarios.
  - `'OCT'` para números octales.
  - `'HEX'` para números hexadecimales.
#### **Retorna**
- `int`: El número de entrada convertido a decimal.

### Función: `convertir_a_binario`
Se divide el número decimal entre 2 repetidamente, guardando el resto en cada paso.
Luego, se leen los restos en orden lifo, formando el número binario.
```
Ejemplo:  
  13 → 13 ÷ 2 = 6 resto 1  
  6 ÷ 2 = 3 resto 0  
  3 ÷ 2 = 1 resto 1  
  1 ÷ 2 = 0 resto 1 → Resultado: 1101  
```
#### **Parámetros**
- `int`: Número decimal a convertir.
#### **Retorna**
- `str`: Representación binaria del número.

### Función: `convertir_a_octal`
Se divide el número decimal entre 8 repetidamente, guardando los restos.
Al leer los restos en orden inverso se obtiene el número en base 8 (octal).
```
Ejemplo: 
  78 → 78 ÷ 8 = 9 resto 6
  9 ÷ 8 = 1 resto 1
  1 ÷ 8 = 0 resto 1 → Resultado: 116 
```
#### **Parámetros**
- `int`: Número decimal a convertir.
#### **Retorna**
- `str`: Representación octal del número.

### Función: `convertir_a_hexadecimal`
Se divide el número decimal entre 16 repetidamente, y se toma el resto.
Ese resto se traduce a un dígito hexadecimal (0–9, A–F).
Finalmente, se invierte el orden de los dígitos obtenidos para formar el resultado final.
```
Ejemplo:  
    254 → 254 ÷ 16 = 15 resto 14 → 'E'
    15 ÷ 16 = 0 resto 15 → 'F' → Resultado: 'FE'
```
#### **Parámetros**
- `int`: Número decimal a convertir.
#### **Retorna**
- `str`: Representación hexadecimal del número.

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

### Diccionario: `directions`
Define las direcciones válidas en las que Snake puede moverse dentro del tablero, asociando cada tecla de control con su descripción textual.

 * `'w'`: `'Arriba'` – Movimiento hacia arriba (fila anterior).
 * `'s'`: `'Abajo'` – Movimiento hacia abajo (fila siguiente).
 * `'a'`: `'Izquierda'` – Movimiento hacia la izquierda (columna anterior).
 * `'d'`: `'Derecha'` – Movimiento hacia la derecha (columna siguiente).

### Clase: `Tablero`

#### Constructor `__init__(self, largo, guardias)`
Inicializa el tablero del juego.
##### Parámetros:
* `largo` (int): Número de columnas del tablero.
* `guardias` (int): Número de guardias a colocar en el tablero.
##### Atributos:
* `self.largo`: Almacena el largo del tablero.
* `self.guardias`: Número de guardias a colocar.
* `self.tablero`: Matriz que representa el tablero.
* `self.snake_pos`: Posición inicial de la Snake.
* `self.objetivo_pos`: Posición del objetivo.
* `self.base`: Base del tablero.

#### Método: `generar_tablero(self)`
Genera el estado inicial del tablero.
* Coloca a Snake (`'S'`) en la posición (5, 0).
* Coloca el objetivo (`'*'`) en una posición aleatoria en la última columna.
* Coloca los guardias (`'!'`) en posiciones aleatorias del tablero.

#### Método: `mover_snake`
Mueve a Snake (`'S'`) en una dirección específica, una cantidad determinada de pasos, siempre que no se salga del tablero.
##### Parámetros:
* `direccion` (`str`): Dirección del movimiento. Debe ser una de las siguientes:
  * `'w'`: Mover arriba (norte).
  * `'s'`: Mover abajo (sur).
  * `'a'`: Mover a la izquierda (oeste).
  * `'d'`: Mover a la derecha (este).
* `pasos` (`int`): Cantidad de celdas a moverse en la dirección indicada.
##### Comportamiento:
* Limpia la posición actual de Snake en el tablero.
* Mueve paso a paso en la dirección especificada, sin salirse de los límites del tablero.
* Evalúa en cada paso si snake se encuentra con un elemento interactivo (`!`, `*`).

Actualiza la posición de Snake y la refleja en el tablero.

#### Método: `mostrar(self)`
Muestra el estado actual del tablero por consola, fila por fila.
* Imprime la matriz del tablero con los siguientes símbolos:

  * `'░'`: Espacio libre.
  * `'S'`: Snake.
  * `'*'`: Objetivo.
  * `'!'`: Guardia (obstáculo).

### Función: `victoria`
Muestra un mensaje de victoria al completar la misión con éxito y termina la ejecución del juego.
#### Comportamiento:
* Imprime un arte ASCII celebrando la victoria.
* Muestra un mensaje indicando que la misión fue completada exitosamente.
* Finaliza el programa con `exit(0)`.

### Función: `derrota`
Muestra un mensaje de derrota cuando Snake es detectado por un guardia o falla el hackeo y finaliza el juego.
#### Comportamiento:
* Imprime un arte ASCII indicando fallo en la misión.
* Muestra un mensaje de alerta informando que Snake fue detectado.
* Finaliza el programa con `exit(0)`.

### Función: `main`
Inicia el entorno, solicita configuraciones iniciales y gestiona el ciclo principal de juego.
#### Comportamiento:
* Da la bienvenida al jugador.
* Solicita al usuario el largo del pasillo (número de columnas del tablero).
* Solicita el número de guardias a colocar en el tablero.
* Crea una instancia de Tablero con los parámetros ingresados.
* Entra en un ciclo donde:
  * Muestra el estado actual del tablero.
  * Solicita al jugador una dirección de movimiento (`w`, `s`, `a`, `d`).
  * Verifica que la dirección sea válida.
  * Solicita la cantidad de pasos a moverse, en una base numérica específica (`BIN`, `OCT`, o `HEX`) definida en el tablero.
  * Convierte el número ingresado a decimal usando la función `convertir_a_decimal`.
  * Mueve a Snake usando el método `mover_snake`.
#### Entradas del Usuario:
 * Largo del tablero (`entero`).
 * Número de guardias (`entero`).
 * Dirección del movimiento (`w`, `s`, `a`, `d` o `-1` para salir).
 * Número de pasos (en base `BIN`, `OCT` o `HEX`).
#### Salida:
 * Muestra el estado del tablero tras cada turno.
 * Mensajes de error si la entrada no es válida.
 * Mensajes de victoria o derrota al finalizar el juego.
## Contacto
* **Sebastián Richiardi**, Rol; 20203055-2, Paralelo: 201
* **Gabriel Alejandro Toro Varela**, Rol; 202204557-4, Paralelo: 201
