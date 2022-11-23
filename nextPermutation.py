# coding: utf-8

def nextPermutation(nums: list) -> list:
    def reverse(arr :list,start :int):
        arrLen = len(arr)
        j = arrLen-1
        for i in range(start,arrLen):
            swap(arr,i,j)
            j-=1
            if i >= j:break
    
    def swap(arr :list, first :int, second :int):
        a = arr[first]
        b = arr[second]
        arr[second] = a
        arr[first] = b
        
    numsLen = len(nums)
    if numsLen <= 1:return nums
    i = numsLen - 1
    while i > 0 and nums[i] <= nums[i-1]:i-=1
    if i > 0:
        j = i
        while j < numsLen and nums[j] > nums[i-1]:j+=1
        swap(nums,i-1,j-1)
    reverse(nums,i)

