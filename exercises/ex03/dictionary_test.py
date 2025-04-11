"""Unit tests module."""

__author__ = "730710469"
import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use_case_1() -> None:
    """this is a Test invert with usual input."""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_use_case_2() -> None:
    """this will test invert with a individual pair."""
    assert invert({"banana": "orange"}) == {"orange": "banana"}


def test_invert_edge_case() -> None:
    """this will test invert raise KeyError for same type values."""
    with pytest.raises(KeyError):
        invert({"x": "1", "y": "1"})


def test_count_use_case_1() -> None:
    """this will test a count with a small list."""
    assert count(["a", "b", "a", "c"]) == {"a": 2, "b": 1, "c": 1}


def test_count_use_case_2() -> None:
    """this will test a count with another list."""
    assert count(["x", "y", "x", "z"]) == {"x": 2, "y": 1, "z": 1}


def test_count_edge_case() -> None:
    """this will test a count with empty list."""
    assert count([]) == {}


def test_favorite_color_use_case_1() -> None:
    """this will test when all have distinct same color."""
    assert favorite_color({"X": "blue", "Y": "blue"}) == "blue"


def test_favorite_color_use_case_2() -> None:
    """this will test when one color is most popular over others ."""
    assert favorite_color({"X": "red", "Y": "red", "Z": "blue"}) == "red"


def test_favorite_color_edge_case() -> None:
    """this will test tie returns of the different color."""
    assert favorite_color({"X": "red", "Y": "blue"}) == "red"


def test_bin_len_use_case_1() -> None:
    """this will test bin_len with different unouts."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_2() -> None:
    """this will test bin_len with duplicate words."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_case() -> None:
    """this will test bin_len with empty list."""
    assert bin_len([]) == {}
