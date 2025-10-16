from src.tp2.crypto import crypt

def test_crypt_pas_1_retourne_chaine():
    res = crypt("Ab9!")
    assert isinstance(res, str)
    assert res != "Ab9!"
