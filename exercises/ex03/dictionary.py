"""Module containing dictionary."""

__author__ = "730710469"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """this function inverts the keys and values from a dictionary also raising KeyError for same values."""
    inverted = {}
    for key in input_dict:
        value = input_dict[key]
        if value in inverted:
            raise KeyError("Duplicate value encountered during inversion")
        inverted[value] = key
    return inverted


def count(values: list[str]) -> dict[str, int]:
    """this function Counts the amount of times each value appears for each input."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(color_dict: dict[str, str]) -> str:
    """this function returns the most popular colors."""
    if not color_dict:
        return ""

    color_count = {}
    for name in color_dict:
        color = color_dict[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    max_count = 0
    popular_color = ""
    for color in color_count:
        if color_count[color] > max_count:
            max_count = color_count[color]
            popular_color = color
    return popular_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """this function will group words by their length and turn them into a dictionary."""
    bins = {}
    for word in words:
        length = len(word)
        if length not in bins:
            bins[length] = set()
        bins[length].add(word)
    return bins
