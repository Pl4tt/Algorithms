def part(arr, low, high):
    pivot = arr[high]
    low_cache = low
    high_cache = high

    while low < high:
        while low < high_cache and arr[low] < pivot:
            low += 1
        
        while high >= low_cache and arr[high] >= pivot:
            high -= 1
        
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    
    if arr[low] > pivot:
        arr[low], arr[high_cache] = arr[high_cache], arr[low]
    
    return low

def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot = part(arr, low, high)
        quicksort(arr, pivot+1, high)
        quicksort(arr, low, pivot-1)
    
    return arr
