#include "utils.c"


void bubble_sort(int arr[], int size) {
    for (int j = 0; j < size; j++) {
        for (int i = 0; i < size-j-1; i++) {
            if (arr[i] > arr[i+1]) {
                swap(&arr[i], &arr[i+1]);
            }
        }
    }
}




int main()
{
    print_array(arr, LENGTH);
    bubble_sort(arr, LENGTH);

    print_array(arr, LENGTH);
    printf("%s", equal_arrays(arr, sol, LENGTH) ? "true" : "false");

    return 0;
}