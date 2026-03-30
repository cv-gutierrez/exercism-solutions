"""Responses."""

def response(hey_bob):
    """lo que sea
    
    :param hey_bob: string - text.
    """
    
    without_whitespace=hey_bob.strip()
    is_question=without_whitespace.endswith("?")
    has_letters=any(char.isalpha() for char in without_whitespace)
    is_shouting= has_letters and without_whitespace.upper()==without_whitespace
    
    if len(without_whitespace)==0:
        return "Fine. Be that way!" 

    if is_shouting and not is_question:
        return "Whoa, chill out!"
    
    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    
    if is_question:
        return "Sure."
    
    return "Whatever." 
