def larger_number(f, g):
    """
    Checks the bigger number
      example:
      larger_number(lambda: 6, lambda: 10)
      larger_number(lambda: 6, lambda: 6)
      larger_number(lambda: 26, lambda: 18)
    """
    if f() > g():
        return "f"
    elif g() > f():
        return "g"
    else:
        return "neither"