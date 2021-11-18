#include "utils.c"


void bubbleSort(int arr[], int size) {
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
    printArray(arr, LENGTH);
    bubbleSort(arr, LENGTH);

    printArray(arr, LENGTH);
    printf("%s", equalArrays(arr, sol, LENGTH) ? "true" : "false");

    return 0;
}