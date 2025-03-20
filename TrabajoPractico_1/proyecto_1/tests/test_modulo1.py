# Archivo de test para realizar pruebas unitarias del modulo1
from modules.modulo1 import obtenerlistadoscores
RUTA2 = "./data/" # Ruta al directorio donde se encuentran los datos txt en general
ARCHIVO2 = RUTA2 + "SCORES.TXT" # Ruta completa para txt con resultados
listadoscores=obtenerlistadoscores(ARCHIVO2)
print(listadoscores)