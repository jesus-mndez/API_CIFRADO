"""
Aqui se prueba el modulo de desencriptado de texto
"""
import pytest
from cryptography.fernet import Fernet
from app.funciones.encriptado import desencriptado_texto

@pytest.mark.parametrize(  # noqa: F821
    "mensaje",
    [
        (b"a"),
        (b"A"),
        (b"mensaje"),
        (b"MeNsAjE"),
        (b"@"),
        (b"este es un mens@je"),
        (b"M3ns@j3 d3 pru3b4!!"),
    ]
)
def test_desencriptando_texto(mensaje)-> str:
    """funcion para probar la desencriptacion

    Args:
        mensaje (_type_): Mensaje a ser encriptado y desencriptado
    """
    llave : str = Fernet.generate_key()
    entorno_cifrado =  Fernet(llave)
    mensaje_encriptado = entorno_cifrado.encrypt(mensaje)
    mensaje_desencriptado: str = desencriptado_texto(mensaje_encriptado, llave)
    assert mensaje_desencriptado == mensaje
