# coding: utf-8

def binarySearch(searched ,targetList: list,descending=False) -> int:
    leftEdge = 0
    rightEdge = len(targetList)-1
    mdIndex = (leftEdge+rightEdge)//2
    while leftEdge < rightEdge-1:
        compareVal = searched - targetList[mdIndex]
        if compareVal == 0:return mdIndex
        if descending:compareVal -= compareVal*2
        if compareVal > 0:
            leftEdge = mdIndex
        else:
            rightEdge = mdIndex
        mdIndex = (leftEdge+rightEdge)//2
        
    return -1