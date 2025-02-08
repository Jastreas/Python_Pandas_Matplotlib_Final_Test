from pyfiglet import Figlet
from colorama import Fore

# Configuración de colores
colorRed = Fore.RED
colorWhite = Fore.WHITE
colorCyan = Fore.BLUE

# Mostrar el encabezado
f = Figlet(font='slant')
print(colorCyan + f.renderText("NUMCAL"))

# Inicialización de variables
pares = impares = suma_pares = suma_impares = 0

def procesar_numero(num):
    global pares, impares, suma_pares, suma_impares
    if num % 2 == 0:
        pares += 1
        suma_pares += num
    else:
        impares += 1
        suma_impares += num

# Bucle principal para pedir números
while True:
    try:
        num = int(input(colorWhite + "Introduce un número entero (0 para salir): "))
        if num == 0:
            break  # Salir del bucle si el número es 0
        procesar_numero(num)  # Procesar el número introducido
    except ValueError:
        print(colorRed + "Por favor, introduce un número entero válido.")

# Mostrar los resultados
print(f"Números pares introducidos: {pares}, Suma de pares: {suma_pares}")
print(f"Números impares introducidos: {impares}, Suma de impares: {suma_impares}")