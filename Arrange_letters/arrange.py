def words(letter, position):
    """
    Returns a word according to the desired position
      example
      words(["g", "e", "o"], [0, 1, 2])
      words(["e","l", "l", "o", "h"], [4, 0, 1, 2, 3])
      words(["g", "e", "o"], [1, 0, 2])
    """
    word = ""
    for x in position:
        word = word + letter[x]
    return word

