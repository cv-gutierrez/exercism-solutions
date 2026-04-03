"""ISBN-10 verification
"""

def is_valid(isbn:str):
    """
    A dummy description.
    """
    isbn=isbn.replace("-","")
    if len(isbn)!=10 or (isbn[-1] not in ("0123456789X")):
        return False
    total=0
    for index in range(10,0,-1):
        digit=isbn[10-index]
        if digit.isdigit():
            total=total+(index*int(digit))
        elif index==1 and digit=="X":
            total+=10
        else:
            return False
    return total%11==0