import string
_TABLE = string.ascii_letters + string.punctuation + string.digits + " "

def _shift_char(c: str, pas: int) -> str:
    if c not in _TABLE:
        return c
    i = _TABLE.index(c)
    return _TABLE[(i + pas) % len(_TABLE)]

def _unshift_char(c: str, pas: int) -> str:
    if c not in _TABLE:
        return c
    i = _TABLE.index(c)
    return _TABLE[(i - pas) % len(_TABLE)]

def crypt(message: str, pas: int = 1) -> str:
    if not isinstance(pas, int) or pas < 1 or pas > 9:
        raise ValueError("pas doit être un entier entre 1 et 9")
    body = "".join(_shift_char(c, pas) for c in message)
    return body + str(pas)

def decrypt(message: str) -> str:
    if not message:
        return message
    last = message[-1]
    if last not in "123456789":
        raise ValueError("Message chiffré invalide : pas (1..9) manquant en suffixe")
    pas = int(last)
    body = message[:-1]
    return "".join(_unshift_char(c, pas) for c in body)
