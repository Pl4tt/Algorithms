#include <stdio.h>

#include "quicksort.c"


void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("end");
}

int main()
{
    int arr[] = {21561, 9, -124714, 0, -1247, 24171, 21742174, 47421, -7285, 261, 2, 521, 10, 3, 216, 7, 6216, 2, 62161, 7, 68, 9, -83148, -1235, 1, -10, 166, 389, 13, 63, 19361, 32, 7317, 8539, 32732, 24151621, -2, 7327, 2157105, 1235, 852, 121, 21, -100, -124, 23, 742, 7654, 87, 123456, 6543, 21261, 48245, 16, 8765, 987654321, 247, 125, 8421, 942, 532, 913, 126, 274, 135, 100000, 2162, 37272};
    int length = sizeof(arr) / sizeof(int);
    
    quicksort(arr, 0, length);
    printArray(arr, length);

    return 0;
}