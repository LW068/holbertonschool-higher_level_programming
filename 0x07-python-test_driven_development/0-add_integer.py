def add_integer(a, b=98):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a and b must be integers or floats")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
