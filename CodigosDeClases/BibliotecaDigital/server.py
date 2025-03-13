# Ejemplo de aplicación principal en Flask
from flask import render_template, request, redirect, url_for

from modules.config import app
from modules.funciones import agregar_libro_a_lista, cargar_lista_desde_archivo, guardar_libro_en_archivo

# Página de inicio
@app.route('/')
def index():
    return render_template('inicio.html')
@app.route('/agregar', methods=["GET","POST"])
def agregar():
    if request.method == "POST":
        # Procesamos los datos del formulario
        nombre = request.form["input_nombre"]
        autor = request.form["input_autor"]
        calificacion = request.form["input_calif"]
        # Guardamos los datos en el archivo
        guardar_libro_en_archivo(ARCHIVO, nombre, autor, calificacion)
        # Agregamos el libro a la lista
        agregar_libro_a_lista(lista_libros, nombre, autor, calificacion) 
        # Redirigimos a la página de inicio
        return redirect(url_for("index"))  
    return render_template('agregar.html')

@app.route("/listar")
def listar():
    return render_template("listar.html", mi_lista= lista_libros)

RUTA = "./data/"
ARCHIVO = RUTA + "libros_leidos.txt"
lista_libros = [] #lista auxiliar

try:
    cargar_lista_desde_archivo(ARCHIVO, lista_libros)            
except FileNotFoundError:
    with open(ARCHIVO, "w") as archi:
        pass

if __name__ == "__main__":
    app.run(debug=True)