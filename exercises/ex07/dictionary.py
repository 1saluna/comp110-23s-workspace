"""EX07 - Dictionary Functions."""

__author__ = "730572303"


def invert(my_dict: dict[str, str]) -> dict[str,str]: 
    "Makes the key the value and the value the key."
    new_dict: dict[str, str] = dict()
    for key in my_dict:
        if my_dict[key] in new_dict:
            raise KeyError("No two keys can be the same!")
        new_dict[my_dict[key]] = key
    return new_dict


def favorite_color(my_dict: dict[str, str]) -> str:
    """Prints out the color that is shown the most times in the dictionary."""
    frequencies: dict[str, int] = dict()
    for key in my_dict:
        if my_dict[key] in frequencies:
            frequencies[my_dict[key]] += 1
        else: 
            frequencies[my_dict[key]] = 1
    maximum: int = 0
    color: str = ""
    for key in frequencies:
        if frequencies[key] > maximum:
            maximum = frequencies[key]
            color = key
    return color 


def count(my_list: list[str]) -> dict[str, int]:
    """Makes a new dictionary out of a list with how many times the values appear in a list."""
    new_dict: dict[str, int] = dict()
    for num in my_list:
        for key in new_dict:
            my_list[num] = key
            if my_list[key] in new_dict:
                new_dict[my_list[num]] +=1
            else: 
                new_dict[my_list[num]] = 1
    return new_dict