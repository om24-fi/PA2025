# Ejemplo de aplicación principal en Flask
from modules.funciones import crear_lista_usuarios
from flask import Flask, render_template
# Página de inicio
app=Flask(__name__)
@app.route('/')
def inicio():
    return render_template("home.html")
@app.route('/bye')
def bye_world():
    lista_usuarios = crear_lista_usuarios(5)
    return render_template('bye.html', usuarios=lista_usuarios)

@app.route("/user/<name>")
def greet(name):
      return render_template("greet.html", username=name)




if __name__=="__main__":
    app.run(debug=True)