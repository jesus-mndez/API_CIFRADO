"""
Este modulo trabajara una encriptacion simetrica!
"""

from cryptography.fernet import Fernet

def encriptando_texto(mensaje:str, llave: str)->str:
    """
    Esta funcion hace un encriptado simetrico
    parametros:
        -   mensaje (str): Mensaje a encriptar
        -   llave (str): Llave de encriptacion
    retorna:
        -   (str): Mensaje encriptado
    """
    entorno_cifrado:str = Fernet(llave)
    mensaje_encriptado:str = entorno_cifrado.encrypt(mensaje)

    return mensaje_encriptado

def desencriptado_texto(mensaje_encriptado: str, llave: str)->str:
    """Funcion para desencriptar mensaje con llave
    Args:
        mensaje_encriptado (str): Mensaje(raro), Listo para ser traducido
        llave (str): Lleave d eencriptacion

    Returns:
        str: Mensaje desencriptado
    """
    
    entorno_cifrado: str = Fernet(llave)
    mensaje_desencriptado:str = entorno_cifrado.decrypt(mensaje_encriptado)
    return mensaje_desencriptado
