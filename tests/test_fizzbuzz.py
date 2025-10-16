from src.tp2.fizzbuzz import affiche

def test_affiche_sans_param_retourne_chaine_100():
    s = affiche()
    assert isinstance(s, str)
    assert "Fizz" in s and "Buzz" in s and "FrisBee" in s
    assert s.startswith("1")
    assert "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee" in s
py
def test_affiche_avec_n():
    from src.tp2.fizzbuzz import affiche
    assert affiche(15) == "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
