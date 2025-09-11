import pytest
from misaligned import print_color_map, get_color_map, _color_index_to_pair_index


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


def test_color_map_formatting():
    """Test that the color map formatting is properly aligned."""
    color_map = get_color_map()
    
    # All lines should have the same length for proper alignment
    # This test will expose the misalignment bug
    line_lengths = [len(line) for line in color_map]
    first_length = line_lengths[0]
    
    # Check if all lines have the same length (they should be aligned)
    for i, length in enumerate(line_lengths):
        expected_msg = f"Line {i} has length {length}, expected {first_length}"
        assert length == first_length, expected_msg
    
    # Also check that single digits are properly padded
    # Line with index 1 should be same length as line with index 10
    line_1 = color_map[1]  # "1 | White | Orange"
    line_10 = color_map[10]  # "10 | Black | Blue"
    alignment_msg = f"Alignment mismatch: '{line_1}' vs '{line_10}'"
    assert len(line_1) == len(line_10), alignment_msg


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
