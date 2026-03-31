"""
def translate(text):
    pass
"""

def translate(text):
    """ translate string
    :param text: string - texto a traducir.
    :return: string - texto traducido.
    """
    
    vowels = ("a", "e", "i", "o", "u")

    def translate_word(word):
        """Procesa cada palabra del texto
        :param word: string - palabra a traducir.
        :return: string - palabra traducida.
        """
        
        # Rule 1
        if word.startswith(("xr", "yt")) or word[0] in vowels:
            return word + "ay"

        # Rule 3 (qu)
        for i in range(len(word)):
            if word[i] in vowels:
                if word[i] == "u" and i > 0 and word[i-1] == "q":
                    return word[i+1:] + word[:i+1] + "ay"
                return word[i:] + word[:i] + "ay"

        # Rule 4 (y como vocal)
        for i in range(len(word)):
            if word[i] == "y":
                return word[i:] + word[:i] + "ay"

        return word  # fallback

    return " ".join(translate_word(word) for word in text.split())