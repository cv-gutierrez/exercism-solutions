def is_isogram(string):
    """Determine if a word or phrase is an isogram
    :param string: str - phrase or word.
    :return: boolean - True if ok.
    """

    return not any(string.lower().count(letter)>1  and letter not in (" ","-")  for letter in string.lower())
