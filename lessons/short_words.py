"""Short words."""

__author__ = "730572303"


def short_words(my_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list: list[str] = []
    for word in my_list: 
        if len(word) < 5:
            new_list.append(word)
        else:
            print(f"{word} is too long!")
    return new_list