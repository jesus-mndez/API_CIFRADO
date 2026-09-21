ALFABETO: str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrado_cesar(texto: str, clave: int)->str:
    """
    Esta funcion genera un cifrado cesar apartir de un mensaje

    Args:
        mensaje (str): El mensaje a ser cifrado
        clave (int): clave de cifrado 
    Return:
        texto_cifrado (str): El texto ya cifrado
    """

    texto_cifrado: str = ""

    for letra in texto.upper():
        if letra in ALFABETO:
            posicion: int = ALFABETO.index(letra)
            nueva_posicion: int = (posicion + clave) % len(ALFABETO)
            nueva_letra: int = ALFABETO[nueva_posicion]
            texto_cifrado += nueva_letra
        else:
            texto_cifrado += letra

    return texto_cifrado
