void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int partition(int array[], int low, int high) {
    int pivot = array[high];
    int i = (low - 1);

    for (int pos = low; pos < high; pos++) {
        if (array[pos] <= pivot) {
            i++;
            swap(&array[i], &array[pos]);
        }
    }

    swap(&array[i + 1], &array[high]);
    
    return (i + 1);
}

void quicksort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);

        quicksort(arr, low, pivot-1);
        quicksort(arr, pivot+1, high);
    }
}



