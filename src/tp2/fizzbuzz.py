from typing import Optional

def _token(n: int) -> str:
    if n % 15 == 0:
        return "FrisBee"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def affiche(n: Optional[int] = None, n2: Optional[int] = None):
    if n is None and n2 is None:
        start, end = 1, 100
    elif n is not None and n2 is None:
        start, end = 1, int(n)
    else:
        start, end = 1, 100
    return "".join(_token(i) for i in range(start, end + 1))
