from flask import Flask, render_template, request, redirect, url_for
from modules.config import app # Importa la instancia de la aplicación Flask desde modules/config.py
from modules.modulo1 import obtenerlistadopeliculas, obtener_pregunta # Importa la función para obtener la lista de películas


# Definición de rutas y nombres de archivos
RUTA = "./data/" # Ruta al directorio donde se encuentran los datos
ARCHIVO = RUTA + "frases_de_peliculas.txt" # Ruta completa al archivo de frases de películas

# Ruta principal ('/')
@app.route('/', methods=['GET', 'POST']) # Define la ruta principal y los métodos permitidos (GET y POST)
def index():
    """
    Función que se ejecuta cuando el usuario visita la página principal.
    Si la solicitud es POST (formulario enviado), redirige al juego.
    Si es GET (carga inicial), muestra la página de inicio.
    """
    if request.method == 'POST': # Si el método de la solicitud es POST
        usuario = request.form['input_usuario'] # Obtiene el nombre del usuario del formulario
        intentos = int(request.form['input_intentos']) # Obtiene el número de intentos del formulario
        peliculas = obtenerlistadopeliculas(ARCHIVO) # Obtiene la lista de películas del archivo
        # Redirige al juego, pasando la información como parámetros en la URL
        return redirect(url_for('jugar', usuario=usuario, intentos=intentos, puntaje=0, jugadas=0, peliculas=",".join(peliculas)))
    return render_template('inicio.html') # Muestra la página de inicio

# Ruta del juego ('/jugar')
@app.route('/jugar') # Define la ruta del juego
def jugar():
    """
    Función que maneja la lógica del juego.
    Obtiene la información del juego de los parámetros de la URL.
    Si aún hay jugadas disponibles, muestra una pregunta.
    Si no, redirige a la página de resultados.
    """
    usuario = request.args.get('usuario') # Obtiene el nombre del usuario de la URL
    intentos = int(request.args.get('intentos')) # Obtiene el número de intentos de la URL
    puntaje = int(request.args.get('puntaje')) # Obtiene el puntaje actual de la URL
    jugadas = int(request.args.get('jugadas')) # Obtiene el número de jugadas realizadas de la URL
    peliculas = request.args.get('peliculas').split(",") # Obtiene la lista de películas de la URL

    if jugadas < intentos: # Si aún hay jugadas disponibles
        jugadas += 1 # Incrementa el contador de jugadas
        frase, pelicula_correcta, peliculas_opciones = obtener_pregunta(ARCHIVO, peliculas) # Obtiene una pregunta aleatoria
        # Muestra la página del juego, pasando la información a la plantilla
        return render_template('juego.html', usuario=usuario, intentos=intentos, puntaje=puntaje, jugadas=jugadas, frase=frase, pelicula_correcta=pelicula_correcta, peliculas=peliculas_opciones)
    else: # Si no hay más jugadas
        # Redirige a la página de resultados, pasando la información a la URL
        return redirect(url_for('resultado', usuario=usuario, puntaje=puntaje, intentos=intentos))

# Ruta para verificar la respuesta ('/verificar')
@app.route('/verificar', methods=['POST']) # Define la ruta para verificar la respuesta y el método permitido (POST)
def verificar():
    """
    Función que verifica la respuesta del usuario.
    Obtiene la información del juego y la respuesta del formulario.
    Actualiza el puntaje si la respuesta es correcta.
    Redirige al juego para la siguiente pregunta.
    """
    usuario = request.form['usuario'] # Obtiene el nombre del usuario del formulario
    intentos = int(request.form['intentos']) # Obtiene el número de intentos del formulario
    puntaje = int(request.form['puntaje']) # Obtiene el puntaje actual del formulario
    jugadas = int(request.form['jugadas']) # Obtiene el número de jugadas realizadas del formulario
    peliculas = request.form['peliculas'].split(",") # Obtiene la lista de películas del formulario
    pelicula_correcta = request.form['pelicula_correcta'] # Obtiene la película correcta del formulario
    pelicula_seleccionada = request.form['pelicula'] # Obtiene la película seleccionada por el usuario del formulario

    if pelicula_seleccionada == pelicula_correcta: # Si la respuesta es correcta
        puntaje += 1 # Incrementa el puntaje
    # Redirige al juego, pasando la información a la URL
    return redirect(url_for('jugar', usuario=usuario, intentos=intentos, puntaje=puntaje, jugadas=jugadas, peliculas=",".join(peliculas)))

# Ruta para mostrar los resultados ('/resultado')
@app.route('/resultado') # Define la ruta para mostrar los resultados
def resultado():
    """
    Función que muestra la página de resultados.
    Obtiene el puntaje final y otra información del juego de la URL.
    """
    usuario = request.args.get('usuario') # Obtiene el nombre del usuario de la URL
    puntaje = int(request.args.get('puntaje')) # Obtiene el puntaje final de la URL
    intentos = int(request.args.get('intentos')) # Obtiene el número de intentos de la URL
    # Muestra la página de resultados, pasando la información a la plantilla
    return render_template('resultado.html', usuario=usuario, puntaje=puntaje, intentos=intentos)

# Ruta para listar las películas ('/listar')
@app.route("/listar") # Define la ruta para listar las películas
def listar():
    """
    Función que muestra la lista de películas.
    Obtiene la lista de películas del archivo.
    """
    listadopeliculas = obtenerlistadopeliculas(ARCHIVO) # Obtiene la lista de películas
    # Muestra la página de la lista de películas, pasando la lista a la plantilla
    return render_template("listar.html", listado=listadopeliculas)


@app.route('/scores', methods=['GET', 'POST'])
def scores():
    return render_template('scores.html')
# Ejecución de la aplicación
if __name__ == "__main__":
    app.run(debug=True) # Inicia el servidor Flask en modo de depuración