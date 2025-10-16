from src.tp2.crypto import crypt

def test_crypt_pas_1_retourne_chaine():
    res = crypt("Ab9!")
    assert isinstance(res, str)
    assert res != "Ab9!"
def test_crypt_avec_pas_et_suffixe():
    from src.tp2.crypto import crypt
    res = crypt("Test 123", 3)
    assert res.endswith("3")
    assert len(res) == len("Test 123") + 1
from src.tp2.crypto import decrypt, crypt

def test_decrypt_inverse_crypt():
    msg = "Hello, World! 42"
    for p in range(1, 10):
        enc = crypt(msg, p)
        dec = decrypt(enc)
        assert dec == msg

def test_decrypt_invalide_si_pas_absent():
    try:
        decrypt("abcdef")
        assert False, "devait lever ValueError si suffixe manquant"
    except ValueError:
        assert True
