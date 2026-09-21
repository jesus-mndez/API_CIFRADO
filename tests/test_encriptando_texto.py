"""
Prueba de la funcion de encriptado simetrico
"""

import pytest
from cryptography.fernet import Fernet
from app.funciones.encriptado import encriptando_texto

@pytest.mark.parametrize(
    "mensaje, llave",
    [
        (b"a", b"Y2j7M6xN0dGQmJ8mJgS6Qj7yYf4vG5mN4iXk4N7C2wQ="),
        (b"b", b"Y2j7M6xN0dGQmJ8mJgS6Qj7yYf4vG5mN4iXk4N7C2wQ="),
    ]
)
def test_encriptado_texto(mensaje: str, llave: str):
    """Funciona para encriptacion de textos

    Args:
        mensaje (str): Mensaje a encriptar
        llave (str): llave de encriptacion
    """
    entorno_cifrado = Fernet(llave)
    salida = encriptando_texto(mensaje = mensaje, llave = llave)
    mensaje_desencriptado = entorno_cifrado.decrypt(salida)
    assert  mensaje == mensaje_desencriptado
