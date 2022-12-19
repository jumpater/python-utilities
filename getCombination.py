# coding: utf-8
# 重複なし組み合わせ、順列

def getCombination(itr , num :int, distinct: bool=True) ->list:
    combs = []
    itrLen = len(itr)
    n = 1 << itrLen
    for i in range(n):
        bit_str = format(i,'b')
        if bit_str.count('1') != num: continue
        bit_str = bit_str.zfill(itrLen)
        comb = []
        for j in range(itrLen):
            if bit_str[j] == '1': comb.append(itr[j])
        if len(comb) == num:
            if distinct: comb.sort()
            if comb in combs:continue
            combs.append(comb)
    return combs

# 重複なし組み合わせ、順列

def getDuplicatedComb(itr , num :int,distinct: bool =True) -> list:
    combs = []
    itrLen = len(itr)
    bitLen = itrLen*num
    n = 1 << bitLen
    for i in range(n):
        bit_str = format(i,'b')
        if bit_str.count('1') != num: continue
        bit_str = bit_str.zfill(bitLen)
        comb = []
        for j in range(bitLen):
            if bit_str[j] == '1': comb.append(itr[(j%itrLen)])
        if len(comb) == num:
            if distinct: comb.sort()
            if comb in combs:continue
            combs.append(comb)
    return combs

# print(len(getCombination([1,2,3,4,5,6,7,8,9,10],6)))
            