"""Odds and evens."""

__author__: "730572303"

def odd_and_even(odd_and_even: list[int]) -> list[int]:
    """Testing for odds and evens."""
    elem: int = 0
    new_list: list[int] = []

    while elem < len(new_list):
        if odd_and_even[elem] % 2 == 1 and elem % 2 == 0:
            new_list.append(odd_and_even[elem])
        elem += 1
    
    return new_list