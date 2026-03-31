"""Raindrops 
"""

def convert(number):
    """Convert number into string.
    :param number: int - number to evaluate.
    :return: string - pling.
    """
    result=""
    if  number%3==0:
        result+= "Pling"
    if number%5==0:
        result+= "Plang"

    if number%7==0:
        result+= "Plong"
        
    if result=="":
        result= str(number)

    return result
