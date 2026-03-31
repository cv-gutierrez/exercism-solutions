"""
def translate(text):
    pass
"""

def translate(text):
    """ translate string
    :param text: string - text to translate.
    :return: string - text traslated.
    """
    
    vowels = ("a", "e", "i", "o", "u")

    def translate_word(word):
        """evaluate each word.
        :param word: string - word to translate.
        :return: string - after translate word.
        """
        
        # Rule 1
        if word.startswith(("xr", "yt")) or word[0] in vowels:
            return word + "ay"

         # Rule 3 (qu)
        for index,letter in enumerate(word):
            if letter in vowels:
                if letter == "u" and index > 0 and word[index-1] == "q":
                    return word[index+1:] + word[:index+1] + "ay"
                return word[index:] + word[:index] + "ay"

        # Rule 4 (y como vocal)
        for index, letter in enumerate(word):
            if letter == "y":
                return word[index:] + word[:index] + "ay"

        return word  # fallback

    return " ".join(translate_word(word) for word in text.split())