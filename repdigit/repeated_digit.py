def repdigit(num):
    """
    Checks if a digit is repeated
      example:
      88
      78
      888

    """

    if int(num) < 0:
        return 'false'
    else:
        if len(num) == 1:
            return 'True'
        else:
            first_digit = num[0]
            for i in num:
                if i != first_digit:
                    print('False')
                    break
            else:
                return 'True'

num = input('write a repdigit')
print(repdigit(num))