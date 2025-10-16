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
