"""
Check parentheses, brackets and braces
"""

def is_paired(input_string):
    """dummy comment.
    """
    
    pila=[]
    #dictonary par
    pares={"}":"{",")":"(","]":"["}
    
    for character in input_string:
        if character in "{([":
            pila.append(character)
        elif character in "})]":
            if not pila or pila.pop()!=pares[character]:
                return False
    return len(pila)==0   
