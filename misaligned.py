"""
This module provides functionality to map major
and minor colors to their respective indices
and print a color map.
"""


def _color_index_to_pair_index(major_index, minor_index):
    """
    Returns the index of a color pair
    given major and minor color indices.
    """
    if major_index < 0 or major_index >= 5 \
       or minor_index < 0 or minor_index >= 5:
        raise ValueError("Invalid color index")
    return major_index * 5 + minor_index


def print_color_map():
    """Prints a color map of major and minor colors."""
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            index = _color_index_to_pair_index(i, j)
            print(f'{index} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


def test_print_color_map():
    """Test the print_color_map function."""
    assert print_color_map() == 25


def test_color_index_to_pair_index_within_range():
    """Test the _color_index_to_pair_index function with valid indices."""
    assert _color_index_to_pair_index(0, 0) == 0
    assert _color_index_to_pair_index(1, 1) == 6
    assert _color_index_to_pair_index(4, 4) == 24


def test_color_index_to_pair_index_out_of_range():
    """
    Test the _color_index_to_pair_index function with out of range indices.
    """
    try:
        _color_index_to_pair_index(5, 0)
    except ValueError:
        pass
    try:
        _color_index_to_pair_index(0, 5)
    except ValueError:
        pass


def test_color_index_to_pair_index_negative():
    """
    Test the _color_index_to_pair_index function with negative indices.
    """
    try:
        _color_index_to_pair_index(-1, 0)
    except ValueError:
        pass
    try:
        _color_index_to_pair_index(0, -1)
    except ValueError:
        pass


if __name__ == "__main__":
    test_print_color_map()
    test_color_index_to_pair_index_within_range()
    test_color_index_to_pair_index_out_of_range()
    test_color_index_to_pair_index_negative()
    print("All tests passed!")
