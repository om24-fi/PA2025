# Ejemplo de aplicación principal en Flask
from flask import render_template
from modules.config import app
from modules.funciones import agregar_libro_a_lista, cargar_lista_desde_archivo, guardar_libro_en_archivo

# Página de inicio
@app.route('/')
def index():
    return render_template('inicio.html')
@app.route('/agregar')
def agregar():
    return render_template('agregar.html')
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