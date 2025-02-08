from pyfiglet import Figlet
from colorama import Fore

#Colores
colorRed = Fore.RED
colorWhite = Fore.WHITE
colorCyan = Fore.BLUE
colorGreen = Fore.GREEN

#heading
f = Figlet(font='slant')
print(colorCyan, f.renderText("Monedatron"))

def calcular_cambio(precio, cantidad_entregada):
    # Monedas Disponibles
    monedas = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    
    # Calcular el cambio a devolver
    cambio = cantidad_entregada - precio
    
    # Comprobar que la cantidad entregada es mayor que el precio
    if cambio < 0:
        print(colorRed + "La cantidad entregada no es suficiente para cubrir el precio.")
        return

    print(colorGreen, f"El cambio a devolver es: {cambio} €")
    
    # Calcular el número de monedas
    for moneda in monedas:
        cantidad_monedas = int(cambio // moneda)
        if cantidad_monedas > 0:
            print(colorCyan + f"{cantidad_monedas} monedas de {moneda}€")
            cambio -= cantidad_monedas * moneda

# Pedir los datos al usuario
precio = float(input(colorWhite + "Introduce el precio del artículo: "))
cantidad_entregada = float(input(colorWhite + "Introduce la cantidad entregada por el cliente: "))

calcular_cambio(precio, cantidad_entregada)

print(colorWhite + "Gracias Por Usar!")