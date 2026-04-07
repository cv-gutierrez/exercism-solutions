"""def rebase(input_base, digits, output_base):
    if input_base
"""

def rebase(input_base, digits, output_base):
    """Dummy comment
    """
    
    if input_base<2:
        raise ValueError("input base must be >= 2")
    if output_base<2:
        raise ValueError("output base must be >= 2")
    result=any( digit<0 or digit >=input_base  for digit in digits)
    if result:
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    if output_base==10:
        return [int(digit) for digit in str(convert_to_decimal(input_base,digits))]
    
    return convert_x_base(convert_to_decimal(input_base,digits),output_base)
    

def convert_x_base(decimal_number,output_base):
    """convert a decimal number into output_base
    """
    remainder=[]
    while decimal_number >= output_base:
        remainder.append(decimal_number%output_base)
        decimal_number=(decimal_number//output_base)
    remainder.append(decimal_number)
    return remainder[::-1]
    
def convert_to_decimal(input_base,digits):
    """Convert digits into a decimal number
    """
    power=len(digits)-1
    total=0
    for digit in digits:
        total+=(digit*(input_base**power))
        power-=1
    return total