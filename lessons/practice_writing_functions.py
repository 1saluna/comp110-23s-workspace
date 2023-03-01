def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Given the string my_words, outputs the same string"""
    if letter_idx >= len(my_words):
        return("Index too high")
    #if we made it here, that means the letter index is valid
    return my_words[letter_idx]