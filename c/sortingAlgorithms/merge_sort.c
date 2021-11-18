#include "utils.c"


void merge(int arr[], int low, int middle, int high) {
    int l = low;
    int h = middle;
    int index = 0;
    
    int result[LENGTH] = {0};

    while (l < middle && h < high) {
        if (arr[l] > arr[h]) {
            result[index] = arr[h];
            h++;
        } else {
            result[index] = arr[l];
            l++;
        }
        index++;
    }

    while (l < middle) {
        result[index] = arr[l];
        index++;
        l++;
    }
    
    while (h < high) {
        result[index] = arr[h];
        index++;
        h++;
    }

    for (int i = low; i < high; i++) {
        arr[i] = result[i-low];
    }
}

void merge_sort(int arr[], int low, int high) {
    int middle = (int) (low + high) / 2;
    
    if (low == middle) return;

    merge_sort(arr, middle, high);
    merge_sort(arr, low, middle);
    
    merge(arr, low, middle, high);
}

int main()
{
    print_array(arr, LENGTH);
    merge_sort(arr, 0, LENGTH);
    
    print_array(arr, LENGTH);
    printf("%s", equal_arrays(arr, sol, LENGTH) ? "true" : "false");

    return 0;
}