import pandas as pd
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
print(colorCyan, f.renderText("Ejercicio 5"))

# Cargar el archivo CSV en un dataframe
try:
    df = pd.read_csv('emisiones.csv')
except:
    print(colorRed, "El archivo no se ha podido cargar...")
    
# Mostrar info del DF
print(colorWhite, "Información del dataframe:")
print(df.info())

# Mostrar primeros 5 registros del DF
print(colorWhite, "\nPrimeros 5 registros del dataframe:")
print(df.head())

# Mostrar el tamaño en memoria del dataframe
print(colorWhite, "\nEspacio que ocupa en memoria:")
print(df.memory_usage(deep=True))

# Obtener los países únicos
paises_unicos = df['Country'].unique()

# Mostrar la cantidad de países diferentes
print(f"Cantidad de países diferentes: {len(paises_unicos)}")

# Mostrar todos los países únicos
print("\nLista de todos los países en el fichero:")
print(paises_unicos)

# Agrupar por país y calcular la media de las emisiones
df_media_emisiones = df.groupby('Country')['Emission'].mean().reset_index()

# Mostrar el DataFrame con las medias de emisiones por país
print("\nDataFrame con la media de emisiones por país:")
print(df_media_emisiones)

df['Emissions_per_capita'] = df['Emission']

# Agrupar por país y obtener la media de las emisiones por habitante
df_media_emisiones_per_capita = df.groupby('Country')['Emissions_per_capita'].mean().reset_index()

# Ordenar los países de mayor a menor contaminación por habitante
df_sorted = df_media_emisiones_per_capita.sort_values(by='Emissions_per_capita', ascending=False)

# Obtener el país más y menos contaminante por habitante
pais_mas_contaminante = df_sorted.iloc[0]
pais_menos_contaminante = df_sorted.iloc[-1]

# Mostrar los resultados
print(f"\nEl país más contaminante es {pais_mas_contaminante['Country']} con unas emisiones de {pais_mas_contaminante['Emissions_per_capita']} toneladas por habitante")
print(f"El país menos contaminante es {pais_menos_contaminante['Country']} con unas emisiones de {pais_menos_contaminante['Emissions_per_capita']} toneladas por habitante")

# Filtrar datos para España y Estados Unidos
df_espana = df[df['Country'] == 'Spain']
df_eeuu = df[df['Country'] == 'United States']

# Calcular la media de emisiones de España y Estados Unidos
media_espana = df_espana['Emission'].mean()
media_eeuu = df_eeuu['Emission'].mean()

# Mostrar las emisiones medias
print(f"\nEmisiones medias de España: {media_espana} toneladas")
print(f"Emisiones medias de Estados Unidos: {media_eeuu} toneladas")

# Lista de países de Sudamérica (asegúrate de que los nombres coincidan con los del archivo)
paises_sudamerica = [
    'Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 
    'Paraguay', 'Perú', 'Surinam', 'Uruguay', 'Venezuela'
]

# Filtrar datos para el año 2011 y países de Sudamérica
df_sudamerica_2011 = df[(df['Year'] == 2011) & (df['Country'].isin(paises_sudamerica))]

# Crear la gráfica de barras con los valores de emisiones para los países sudamericanos en 2011
plt.figure(figsize=(10,6))
plt.bar(df_sudamerica_2011['Country'], df_sudamerica_2011['Emission'], color='green')

# Añadir títulos y etiquetas
plt.title('Emisiones de CO2 por país en Sudamérica (2011)', fontsize=14)
plt.xlabel('País', fontsize=12)
plt.ylabel('Emisiones (Toneladas)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar la gráfica
plt.show()