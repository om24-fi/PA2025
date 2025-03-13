# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el códigode
import random
def crear_lista_usuarios(n_usuarios):
    lista_usuarios=[]
    for i in range(n_usuarios):
           
        usuario = {
            'nombre': f'usuario_{i+1}',
            'edad': random.randint(18, 60)
             }
        lista_usuarios.append(usuario)

    return lista_usuarios