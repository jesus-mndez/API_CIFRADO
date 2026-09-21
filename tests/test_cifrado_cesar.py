from app.funciones.cifrado_cesar import cifrado_cesar
import pytest

@pytest.mark.parametrize(
        "entrada, clave, salida_esperada",
        [
            ("mama",1,"NBNB"),
            ("papa",1,"QBQB"),
            ("A",2,"C"),
            ("z",1,"A"),
            ("Z!",2,"B!"),
            ("@",14,"@"),
            ("mama123",1,"NBNB123"),
        ]
)
def test_cifrado_cesar(entrada,clave,salida_esperada):
    """Test para cifrado cesar"""
    texto_cifrado = cifrado_cesar(texto = entrada, clave = clave)
    assert texto_cifrado == salida_esperada