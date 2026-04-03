""" The Caesar cipher
"""
import string

def rotate(text, key):
    """A dummy comment.
    """
    
    #key=key[3:]
    alphabet=string.ascii_lowercase
    new_text=""
    for letter in text:
        if letter.lower() in alphabet:
            index=alphabet.find(letter.lower())
            new_index= (index+key)%26
            new_text+=alphabet[new_index] if letter.islower() else alphabet[new_index].upper()
        else:
            new_text+=letter
    return new_text