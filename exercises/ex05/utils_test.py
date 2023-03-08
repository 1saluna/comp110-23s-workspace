"""Testing if the functions work."""

__author__ = "730572303"

from ex05.utils import only_evens, concat, sub

def test_evens() -> None:
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]

def test_odds() -> None:
    test_list: list[int] = [3, 5, 7]
    assert only_evens(test_list) == []

def test_empty_evens() -> None:
    test_list: list[int] = []
    assert only_evens(test_list) == []

#from exercises.ex05.utils import concat

def test_twolists() -> None:
    l1: list[int] = [2, 4, 6]
    numbers: list[int] = [3, 2, 1]
    assert concat(l1, numbers) == [2, 4, 6, 3, 2, 1]

def test_empty() -> None: 
    l1: list[int] = []
    numbers: list[int] = []
    assert concat(l1, numbers) == [] 

def test_one_empty() -> None:
    l1: list[int] = [4, 6, 7]
    numbers: list[int] = []
    assert concat(l1, numbers) == [4, 6, 7]

#from exercises.ex05.utils import sub

def test_workingrange() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    num_1: int = 1
    num_2: int = 3
    assert sub(a_list, num_1, num_2) == [20, 30]

def test_emptylist() -> None:
    a_list: list[int] = []
    num_1: int = 1
    num_2: int = 3
    assert sub(a_list, num_1, num_2) == []

def test_start_zero() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    num_1: int = -4
    num_2: int = 3
    assert sub(a_list, num_1, num_2) == [10, 20, 30]