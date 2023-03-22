"""Challenge question 04."""

__author__ = "730572303"

def zip(num1: list[str], num2: list[int]) -> dict[str, int]:
    """Making a new dict."""
    newdict: dict[str, int] = {}
    if len(num1) != len(num2): 
        return {}
    if len(num1) <= 0 and len(num2) <= 0:
        return {}
    for i in range(len(num1)): 
        newdict[num1[i]] = num2[i]
    return newdict