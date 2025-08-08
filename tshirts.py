
def size(cms):
    size_map = {
        range(35, 38): 'S',
        range(38, 42): 'M',
        range(42, 47): 'L'
    }
    size = 'Invalid size'
    for size_range, size_label in size_map.items():
        if cms in size_range:
            size = size_label
            break

    return size


def test_tshirt_size():
    assert(size(37) == 'S')
    assert(size(38) == 'M')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    assert(size(5) == 'Invalid size')
    assert(size(50) == 'Invalid size')
    assert(size(100) == 'Invalid size')
print("All is well (maybe!)")
