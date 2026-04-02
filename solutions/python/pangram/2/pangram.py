"""Pangram"""

def is_pangram(sentence):
    """Return if a sentence is a pangram
    :param sentence: string - text to evaluate.
    :return: boolean - True if all the letter is the sentence."""
    
    alphabet="abcdefghijklmnopqrstuvwxyz"
    sentence=sentence.lower()

    for letter in alphabet:
        if letter not in sentence:
            return False
        
    return True
