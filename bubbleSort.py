# coding: utf-8

def bubbubleSorter(targetList: list,reverse=False) -> list:
    if not len(targetList): return targetList
    
    for i in range(0,len(targetList)-1):
        for j in range(i+1,len(targetList)):
            compareVal = targetList[i] - targetList[j]
            if reverse:compareVal = compareVal - compareVal*2
            if compareVal > 0:
                nowIndexVal = targetList[i]
                targetList[i] = targetList[j]
                targetList[j] = nowIndexVal
    
    return targetList