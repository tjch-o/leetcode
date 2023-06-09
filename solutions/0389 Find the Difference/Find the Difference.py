def findTheDifference(s, t):
    if not s:
        return t

    list1 = list(s)
    list1.sort() 
    list2 = list(t)
    list2.sort()
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return list2[i]
    # since list1 is shorter than list2, if we didnt return an element before the last element is the element added
    return list2[-1] 