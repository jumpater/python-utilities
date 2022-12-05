# coding: utf-8

def nextPermutation(itr) -> list:
    def reverse(arr :list,start :int):
        arrLen = len(arr)
        j = arrLen-1
        for i in range(start,arrLen):
            swap(arr,i,j)
            j-=1
            if i >= j:break
    
    def swap(arr :list, first, second):
        a = arr[first]
        b = arr[second]
        arr[second] = a
        arr[first] = b
        
    numsLen = len(itr)
    if numsLen <= 1:return itr
    i = numsLen - 1
    while i > 0 and itr[i] <= itr[i-1]:i-=1
    if i > 0:
        j = i
        while j < numsLen and itr[j] > itr[i-1]:j+=1
        swap(itr,i-1,j-1)
    reverse(itr,i)

