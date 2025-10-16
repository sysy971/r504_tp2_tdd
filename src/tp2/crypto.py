import string
_TABLE = string.ascii_letters + string.punctuation + string.digits + " "

def _shift_char(c: str, pas: int) -> str:
    if c not in _TABLE:
        return c
    i = _TABLE.index(c)
    return _TABLE[(i + pas) % len(_TABLE)]

def crypt(message: str, pas: int = 1) -> str:
    if not isinstance(pas, int) or pas < 1 or pas > 9:
        raise ValueError("pas doit être un entier entre 1 et 9")
    body = "".join(_shift_char(c, pas) for c in message)
    return body + str(pas)
