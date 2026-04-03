"""ISBN-10 verification
"""

def is_valid(isbn:str):
    """
    A dummy description.
    """
    isbn=isbn.replace("-","")
    if (not len(isbn)==10) or (isbn[-1] not in ("0123456789X")):
        return False
    sum=0
    for index in range(10,0,-1):
        if isbn[10-index] in ("0123456789"):
            sum=sum+(index*int(isbn[10-index]))
        elif index==1 and isbn[10-index]=="X":
            sum=sum+(index*10)
        else:
            return False
    return sum%11==0