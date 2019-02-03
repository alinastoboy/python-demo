def cashback(monthly_expenses):
    """
    >>> cashback(10_000)
    300.0
    """
    percent = 3
    #print('function called')
    result = percent * monthly_expenses / 100
    return result # возврат значения

def bmi(weight, height): # shift + f6
    """
    >>> bmi(106, 1.68) # doctest: +ELLIPSIS
    37.55...
    """
    result = weight / (height ** 2)
    return result