"""Using 'list' Utility Functions."""

__author__ = "730572303"


def all(all: list[int], number: int) -> bool:
    """Seeing if the number being tested is in the list."""
    idx: int = 0
    if len(all) < 1:
        return False
    while idx < len(all):
        if number != all[idx]:
            return False
        if number == all[idx]:
            idx += 1
    return True


def max(max: list[int]) -> int:
    """Testing to see which integer is the largest in a list."""
    idx: int = 0
    maximum: int = max[0]
    if len(max) == 0:
        raise ValueError("max() arg is an empty List")
    while len(max) - 1 > idx:
        if maximum < max[idx + 1]:
            maximum = max[idx + 1]
        idx += 1 
    return maximum 
        

def is_equal(is_equal: list[int], numbers: list[int]) -> bool:
    """Seeing if the two lists are identical."""
    if is_equal == numbers:
        return True
    else:
        return False