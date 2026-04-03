"""ISBN-10 verification
"""

def is_valid(isbn:str):
    """
    """
    isbn=isbn.replace("-","")
    if (not len(isbn)==10) or (isbn[-1] not in ("0123456789X")):
        return False
    sum=0
    for i in range(10,0,-1):
        if isbn[10-i] in ("0123456789"):
            sum=sum+(i*int(isbn[10-i]))
        elif i==1 and isbn[10-i]=="X":
            sum=sum+(i*10)
        else:
            return False
    return sum%11==0