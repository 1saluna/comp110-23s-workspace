"""Testing if the functions work."""

__author__ = "730572303"

from ex05.utils import only_evens, concat, sub


def test_evens() -> None:
    """List with only even numbers."""
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_odds() -> None:
    """List with only odd numbers."""
    test_list: list[int] = [3, 5, 7]
    assert only_evens(test_list) == []


def test_empty_evens() -> None:
    """List with no integers."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


# from exercises.ex05.utils import concat

def test_twolists() -> None:
    """Combing two lists together."""
    l1: list[int] = [2, 4, 6]
    numbers: list[int] = [3, 2, 1]
    assert concat(l1, numbers) == [2, 4, 6, 3, 2, 1]


def test_empty() -> None: 
    """Combining two empty lists."""
    l1: list[int] = []
    numbers: list[int] = []
    assert concat(l1, numbers) == [] 


def test_one_empty() -> None:
    """Combining an empty list with a list of ints."""
    l1: list[int] = [4, 6, 7]
    numbers: list[int] = []
    assert concat(l1, numbers) == [4, 6, 7]


# from exercises.ex05.utils import sub

def test_workingrange() -> None:
    """Testing with a working range of ints."""
    a_list: list[int] = [10, 20, 30, 40]
    num_1: int = 1
    num_2: int = 3
    assert sub(a_list, num_1, num_2) == [20, 30]


def test_emptylist() -> None:
    """Testing with an empty list."""
    a_list: list[int] = []
    num_1: int = 1
    num_2: int = 3
    assert sub(a_list, num_1, num_2) == []


def test_start_zero() -> None:
    """Testing with a start index of a negative number to change to 0."""
    a_list: list[int] = [10, 20, 30, 40]
    num_1: int = -4
    num_2: int = 3
    assert sub(a_list, num_1, num_2) == [10, 20, 30]