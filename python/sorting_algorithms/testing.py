from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quicksort import quicksort
from radix_lsd_sort import radix_lsd_sort, binary_radix_lsd_sort


if __name__ == "__main__":
    easy_sort_test = [9, 6, 8, 2, 3]
    medium_sort_test = [9, 3, 8, 2, 0, -10, 3]
    difficult_sort_test = [21561, 9, -124714, 24171, 21742174, 47421, -7285, 261, 2, 62161, 7, 521, 10, 3, 216, 7, 6216, 2, 68, 9, 0, -1247, -83148, -1235, 166, 389, 1235, 852, 13, 63, 7317, 8539, 32732, 24151621, 2157105, 121, 21, 1, -10, -100, -124, -2, 7327, 23, 19361, 32, 742, 8765, 987654321, 123456, 7654, 87, 6543, 21261, 48245, 16, 247, 942, 532, 913, 126, 274, 135, 100000, 2162, 37272, 125, 8421]
    difficult_sort_test2 = [21561, 9, -124714, 0, -1247, 24171, 21742174, 47421, -7285, 261, 2, 521, 10, 3, 216, 7, 6216, 2, 62161, 7, 68, 9, -83148, -1235, 1, -10, 166, 389, 13, 63, 19361, 32, 7317, 8539, 32732, 24151621, -2, 7327, 2157105, 1235, 852, 121, 21, -100, -124, 23, 742, 7654, 87, 123456, 6543, 21261, 48245, 16, 8765, 987654321, 247, 125, 8421, 942, 532, 913, 126, 274, 135, 100000, 2162, 37272]
    
    difficult_non_negative_sort_test = [5312, 621, 7, 47, 1, 34, 7, 3146134, 416, 21, 641, 3512, 6325, 64174, 326, 3416, 417, 3164, 3421653, 731, 1431, 43181346, 631280]
    print(sorted(difficult_sort_test2))
    print(bubble_sort(difficult_sort_test) == merge_sort(difficult_sort_test) == quicksort(difficult_sort_test2) == sorted(difficult_sort_test2))
    
    print(bubble_sort(difficult_sort_test) == sorted(difficult_sort_test2))
    print(merge_sort(difficult_sort_test) == sorted(difficult_sort_test2))
    print(quicksort(difficult_sort_test) == sorted(difficult_sort_test2))

    print(radix_lsd_sort(difficult_non_negative_sort_test) == sorted(difficult_non_negative_sort_test))
    print(binary_radix_lsd_sort(difficult_non_negative_sort_test) == sorted(difficult_non_negative_sort_test))