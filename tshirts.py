
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
