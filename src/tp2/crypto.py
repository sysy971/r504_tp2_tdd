import string
_TABLE = string.ascii_letters + string.punctuation + string.digits + " "

def _shift_char(c: str, pas: int) -> str:
    if c not in _TABLE:
        return c
    i = _TABLE.index(c)
    return _TABLE[(i + pas) % len(_TABLE)]

def crypt(message: str, pas: int = 1) -> str:
    if not isinstance(pas, int) or pas < 1:
        pas = 1
    return "".join(_shift_char(c, pas) for c in message)
