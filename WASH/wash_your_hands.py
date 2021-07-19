def WYH(n, nM):
    """
    Calculates the minutes and seconds we wash our hands in a month(s)
      Example:
      WYH(7, 9)
      WYH(78, 80)
      WYH(0, 0)
    """
    wash_hands = n * 21
    months = nM * 30
    minutes_to_wash = wash_hands * months
    total_minutes = minutes_to_wash // 60
    seconds = minutes_to_wash % 60
    result = f'{total_minutes}minutes, {seconds}seconds'
    return result
