def valid_pin(pin):
    """
    Checks if a pin is valid and has no white space
      example:
      valid_pin('1234')
      valid_pin('78 98')
      valid_pin('0000')
    """
    if pin == '':
        return 'False'
    return len(pin) in [4, 6] and pin.isdigit()
