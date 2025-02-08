import csv
import random
import matplotlib.pyplot as plt
from pyfiglet import Figlet
from colorama import Fore

#Colores
colorRed = Fore.RED
colorWhite = Fore.WHITE
colorCyan = Fore.BLUE
colorGreen = Fore.GREEN

#heading
f = Figlet(font='slant')
print(colorCyan, f.renderText("Grafica"))

def Crear_Archivo():
    archivo_csv = "Manea_eje3.csv"
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    # Crear y escribir en el archivo CSV
    with open(archivo_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # cabecera
        writer.writerow(["id", "dia", "gastos", "ventas"])
        
        # Generar registros
        for i in range(1, 366):
            dia = dias_semana[(i - 1) % 7]  # Ciclo de días de la semana
            gastos = random.randint(10, 30)
            ventas = random.randint(10, 150)
            
            # Escribir la fila en el CSV
            writer.writerow([i, dia, gastos, ventas])

    print(colorGreen, f"Archivo '{archivo_csv}' generado correctamente.")
    print(colorWhite, "Gracias por usar!")

def Mostrar_Grafica():
    # Nombre del archivo CSV
    archivo_csv = "Manea_eje3.csv"

    # Listas para almacenar datos de la primera semana
    dias = []
    gastos = []
    ventas = []

    # Leer el archivo CSV y extraer datos de la primera semana
    with open(archivo_csv, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera
        
        for i, row in enumerate(reader):
            if i >= 7:  # Solo leer los primeros 7 días
                break
            dias.append(row[1])  # Día de la semana
            gastos.append(int(row[2]))  # Gastos
            ventas.append(int(row[3]))  # Ventas

    # Crear la gráfica
    plt.figure(figsize=(8, 5))
    plt.plot(dias, gastos, marker="o", linestyle="-", label="Gastos", color="red")
    plt.plot(dias, ventas, marker="s", linestyle="--", label="Ventas", color="blue")
    
    # Personalización
    plt.xlabel("Día de la semana")
    plt.ylabel("Cantidad")
    plt.title("Gastos y Ventas en la primera semana")
    plt.legend()
    plt.grid(True)

    plt.show()

Crear_Archivo()
Mostrar_Grafica()