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


def get_color_map():
    """Returns a list of formatted color map strings."""
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    result = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            index = _color_index_to_pair_index(i, j)
            result.append(f'{index} | {major} | {minor}')
    return result


def print_color_map():
    """Prints a color map of major and minor colors."""
    color_map = get_color_map()
    for line in color_map:
        print(line)
    return len(color_map)
