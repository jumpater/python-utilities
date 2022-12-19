# coding: utf-8

def pivot(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        # array[high]がpivot未満の所までhighをデクリメント
        while low <= high and array[high] >= pivot:
            high -= 1
            
        # array[low]がpivotより大きい所までhighをインクリメントする
        while low <= high and array[low] <= pivot:
            low += 1
        
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    # この時のhighはarray[high]がpivot未満での数で、尚且つインデックスが最も大きい
    array[start], array[high] = array[high], array[start]
    return high

def quickSort(array, start, end):
    if start >= end:
        return
    # 並び替え & ピボットのインデックス取得
    p = pivot(array, start, end)
    
    quickSort(array, start, p-1)
    quickSort(array, p+1, end)