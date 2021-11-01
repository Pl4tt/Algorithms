def radix_lsd_sort(arr):
    if len(arr) <= 1:
        return arr
    
    BASE = 10
    max_val = max(arr)
    factor = 1

    while factor <= max_val:
        partition = [[] for _ in range(BASE)]
        for i in arr:
            index = (i//factor) % BASE
            partition[index].append(i)
            
        arr = []
        for i in partition:
            arr.extend(i)
    
        factor *= BASE

    return arr


def binary_radix_lsd_sort(arr):
    if len(arr) <= 1:
        return arr
    
    BASE = 2
    bit_length = max(arr).bit_length()

    for bit in range(bit_length):
        partition = [[] for _ in range(BASE)]
        for i in arr:
            index = (i >> bit) & 1
            partition[index].append(i)
            
        arr = [*partition[0], *partition[1]]

    return arr

    