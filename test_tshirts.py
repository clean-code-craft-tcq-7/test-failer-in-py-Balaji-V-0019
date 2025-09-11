import pytest
from tshirts import size


def test_tshirt_size():
    """Test the basic tshirt size function."""
    assert(size(37) == 'S')
    assert(size(38) == 'M')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    assert(size(5) == 'Invalid size')
    assert(size(50) == 'Invalid size')
    assert(size(100) == 'Invalid size')


def test_tshirt_size_boundary_bug():
    """Test that exposes the missing value bug - size 47 should be 'L' but returns 'Invalid size'."""
    # The L range is defined as range(42, 47) which only goes from 42 to 46
    # Size 47 should also be included in L size
    assert(size(47) == 'L')  # This will fail! 47 is not in range(42, 47)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
    print("All is well (maybe!)")
