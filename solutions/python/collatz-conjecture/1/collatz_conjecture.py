"""Collatz Conjecture.
"""

def steps(number):
    """Avalue Collatz Conjecture.
    
    :param number: int - number to evaluate
    :return: int - steps number to reach 1
    """
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    
    steps_count=0
    while number>1:
        if not number%2:
            number/=2
            steps_count+=1
        else:
            number=(number*3)+1
            steps_count+=1

    return steps_count