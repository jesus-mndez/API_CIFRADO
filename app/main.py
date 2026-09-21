"""
Este es el archivo principal
"""

from funciones.cifrado_cesar import cifrado_cesar

MENSAJE: str = "Hola mundo, estoy en un curso"
CLAVE: int = 7

resultado: str = cifrado_cesar(MENSAJE,CLAVE)
print(resultado) 