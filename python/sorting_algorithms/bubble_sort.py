def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            
    return arr

