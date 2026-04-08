""" Encode / decode Ciphertext
"""
def encode(plain_text):
    """Dummy comment.
    """
    alphabet="abcdefghijklmnopqrstuvwxyz"
    result=""
    clean_text=[character.lower() for character in plain_text if character.isalnum()]
    for character in clean_text:
        if character.isdigit():
            result+=character
        else:
            index_in_alphabet=alphabet.find(character)
            result+=alphabet[25-index_in_alphabet]
    
    return " ".join(result[index:index+5] for index in range(0,len(result),5))

def decode(ciphered_text):
    """Dummy comment.
    """
    cipher="zyxwvutsrqponmlkjihgfedcba"
    result=""
    for character in ciphered_text.lower():
        if character.isdigit():
            result+=character
        elif character==" ":
            continue
        else:
            index_in_alphabet=cipher.find(character)
            result+=cipher[25-index_in_alphabet]
    return result
