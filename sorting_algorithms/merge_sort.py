def merge(arr, low, middle, high):
    l = low
    h = middle

    result = []

    while l < middle and h < high:
        if arr[l] < arr[h]:
            result.append(arr[l])
            l += 1
        else:
            result.append(arr[h])
            h += 1
        
    if l < middle:
        result.extend(arr[l:middle])
    
    if h < high:
        result.extend(arr[h:high])
    
    for i in range(low, high):
        arr[i] = result[i - low]


def split(arr, low, high):
    middle = (low + high) // 2
    
    if low == middle:
        return

    split(arr, middle, high)
    split(arr, low, middle)
    merge(arr, low, middle, high)

def merge_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr)
    
    split(arr, low, high)

    return arr
