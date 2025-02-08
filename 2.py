from pyfiglet import Figlet
from colorama import Fore

#Colores
colorRed = Fore.RED
colorWhite = Fore.WHITE
colorCyan = Fore.BLUE
colorGreen = Fore.GREEN

#heading
f = Figlet(font='slant')
print(colorCyan, f.renderText("SINO"))

def si_o_no(entrada):
    entrada = entrada.strip()  # Elimina espacios al inicio y al final
    opciones_si = {'si', 's', 'Si', 'SI'} #listas de inpValido
    opciones_no = {'no', 'n', 'No', 'NO'} #listas de inpInvalido
    
    if entrada in opciones_si:
        return True
    elif entrada in opciones_no:
        return False
    else:
        print(colorRed + "Por favor introduzca s o n")
        return None

# Solicitar entrada al usuario
while True:
    entrada_usuario = input(colorWhite + "Ingrese 'si' o 'no': ")
    resultado = si_o_no(entrada_usuario)
    
    if resultado is not None:
        print(colorGreen, "s" if resultado else "n")
        break