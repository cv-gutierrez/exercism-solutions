""" Function to evaluate if a number is an Armstrong number.
"""

def is_armstrong_number(number):
    """Evaluate if a given number either Armstrong number or not.
    :param number: int - given number to evaluate.
    :return: boolean - True if the number is Armstrong number.
    """
    string_value=str(number)
    length= len(string_value)
    
    return sum(int(digit)**length for digit in string_value) == number
