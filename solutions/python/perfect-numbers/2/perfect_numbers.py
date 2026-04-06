"""Module providing a function printing python version."""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    
    total=0
    for divisor in range(number-1,0,-1):
        if number%divisor==0:
            total+=divisor
    #perfect
    if total==number:
        return "perfect"
    #abundant
    if total> number:
        return "abundant"
    #deficient
    return "deficient"