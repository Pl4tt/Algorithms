#include "utils.cpp"


int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int l = (low - 1);

    for (int pos = low; pos < high; pos++) {
        if (arr[pos] <= pivot) {
            l++;
            swap(&arr[l], &arr[pos]);
        }
    }
    
    swap(&arr[l+1], &arr[high]);

    return (l + 1);
}

void quicksort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);

        quicksort(arr, pivot+1, high);
        quicksort(arr, low, high-1);
    }
}




int main()
{
    printArray(arr, length);
    
    quicksort(arr, 0, length-1);
    printArray(arr, length);

    cout << (equalArrays(arr, sol, length) ? "true" : "false");

    return 0;
}