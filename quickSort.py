# coding: utf-8

def pivot(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def quickSort(array, start, end):
    if start >= end:
        return
    p = pivot(array, start, end)
    quickSort(array, start, p-1)
    quickSort(array, p+1, end)