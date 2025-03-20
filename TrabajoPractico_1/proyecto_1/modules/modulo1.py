# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
import random
def obtenerlistadopeliculas(ARCHIVO):

    listadopeliculas = [] #lista auxiliar

    with open(ARCHIVO, "r", encoding="utf-8") as archi:
        lineas=archi.readlines()
        lineas = [linea.strip() for linea in lineas]
        lineas = [linea.split(";") for linea in lineas]
        lineas = [linea[1] for linea in lineas]
        lineas = [linea.lower() for linea in lineas ]
        for pelicula in lineas:
            if pelicula not in listadopeliculas:
                listadopeliculas.append(pelicula)

    return sorted(listadopeliculas)

def obtenerlistadoscores(ARCHIVO2):
     with open(ARCHIVO2, "r", encoding="utf-8") as archi2:
        lineas=archi2.readlines()
        lineas = [linea.strip() for linea in lineas]
        
     return lineas
    
# Función para obtener una pregunta aleatoria
def obtener_pregunta(archivo, lista_peliculas):
    """
    Función que selecciona una frase aleatoria, la película correcta y opciones.
    """
    with open(archivo, "r", encoding="utf-8") as f: # Abre el archivo de frases de películas
        lineas = f.readlines() # Lee todas las líneas del archivo
        linea = random.choice(lineas).strip().split(";") # Selecciona una línea aleatoria y la divide en frase y película
        frase = linea[0] # Obtiene la frase
        pelicula_correcta = linea[1].lower() # Obtiene la película correcta
        peliculas_opciones = random.sample(lista_peliculas, 3) # Selecciona 3 películas aleatorias como opciones
        if pelicula_correcta not in peliculas_opciones: # Asegura que la película correcta esté entre las opciones
            peliculas_opciones[random.randint(0, 2)] = pelicula_correcta
        random.shuffle(peliculas_opciones) # Mezcla las opciones desordenando la lista
        return frase, pelicula_correcta, peliculas_opciones # Devuelve la frase, la película correcta y las opciones