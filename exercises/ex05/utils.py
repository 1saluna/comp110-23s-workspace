"""Using utility functions."""

__author__ = "730572303"


def only_evens(only_evens: list[int]) -> list[int]:  # this makes a new list with only the even integers in the given list
    """Making a new list with only the even integers."""
    result: list[int] = list()
    for index in range(len(only_evens)):
        if only_evens[index] % 2 == 0: 
            result.append(only_evens[index])
    return result 


def concat(l1: list[int], numbers: list[int]) -> list[int]:  # this makes a new list with all of the numbers from both of the lists
    """Combining the two lists to make a new big one."""
    new_list: list[int] = list(l1 + numbers)
    return new_list


def sub(a_list: list[int], num_1: int, num_2: int) -> list[int]:  # this makes a new list with integers in the range of indexes given
    """Returning the indexes in the range."""
    new_list: list[int] = list()
    if num_1 < 0:
        num_1 = 0
    if num_2 > len(a_list):
        num_2 = len(a_list) - 1
    if len(a_list) == 0 or num_1 > len(a_list) or num_2 <= 0: 
        return list()
    for idx in range(num_1, num_2): 
        num_2 = num_2 - 1
        new_list.append(a_list[idx])
    return new_list