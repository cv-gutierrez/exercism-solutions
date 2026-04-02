"""Pangram"""

def is_pangram(sentence):
    """Return if a sentence is a pangram
    :param sentence: string - text to evaluate.
    :return: boolean - return True if the sentence is a pangram."""
    
    alphabet="abcdefghijklmnopqrstuvwxyz"
    sentence=sentence.lower()

    for letter in alphabet:
        if letter not in sentence:
            return False
        
    return True