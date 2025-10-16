from src.tp2.fizzbuzz import affiche

def test_affiche_sans_param_retourne_chaine_100():
    s = affiche()
    assert isinstance(s, str)
    assert "Fizz" in s and "Buzz" in s and "FrisBee" in s
    assert s.startswith("1")
    assert "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee" in s

def test_affiche_avec_n():
    from src.tp2.fizzbuzz import affiche
    assert affiche(15) == "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
def test_affiche_intervalle():
    from src.tp2.fizzbuzz import affiche
    assert affiche(5, 10) == "BuzzFizz78FizzBuzz"
    assert affiche(10, 16) == "Buzz11Fizz1314FrisBee16"
