"""EX07 - Unit Tests for Dictionary."""

__author__ = "730572303"

from dictionary import invert, favorite_color, count


def test_invert_letters() -> None:
    """Invert dictionary with letters."""
    test_dict: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(test_dict) == {"b": "a", "d": "c", "f": "e"}


def test_invert_words() -> None:
    """Invert dictionary wih words."""
    test_dict: dict[str, str] = {"sunny": "rainy", "happy": "sad", "easy": "hard"}
    assert invert(test_dict) == {"rainy": "sunny", "sad": "happy", "hard": "easy"}


def test_invert_duplicate() -> None:
    """Invert with two equal keys."""
    test_dict: dict[str, str] = {"a": "b", "c": "d", "e": "c"}
    assert invert(test_dict) == "No two keys can be the same!"


def test_favorite_color_onemax() -> None:
    """One max color in the dict."""
    test_dict: dict[str, str] = {"Isa": "orange", "Chandler": "orange", "Jim": "blue"}
    assert favorite_color(test_dict) == "orange"


def test_favorite_color_clearmax() -> None:
    """One max color in the dict."""
    test_dict: dict[str, str] = {"Isa": "orange", "Chandler": "blue", "Jim": "blue", "Jess": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_twosame() -> None:
    """Two colors are found the most."""
    test_dict: dict[str, str] = {"Isa": "orange", "Chandler": "orange", "Jim": "blue", "Jess": "blue"}
    assert favorite_color(test_dict) == "orange"


def test_count_letters() -> None: 
    """Working list with values in the dictionary."""
    test_list: list[str] = ["a", "a", "b"]
    assert count(test_list) == {"a": 2, "b": 1}


def test_count_names() -> None:
    """Working list with names in the dicitonary."""
    test_list: list[str] = ["Jim", "Isa", "Jim", "Bob", "Jim"]
    assert count(test_list) == {"Jim": 3, "Isa": 1, "Bob": 1}


def test_count_emptylist() -> None:
    """Testing with an empty list given."""
    test_list: list[str] = []
    assert count(test_list) == {}