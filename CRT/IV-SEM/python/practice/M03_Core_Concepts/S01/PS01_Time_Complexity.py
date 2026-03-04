def Linear_Search(element,target):
    for i in range(len(element)):
        if target == element[i]:
            return i
    return -1
print(Linear_Search([12,45,78,69,32],12))
print(Linear_Search([12,45,78,69,32],78))
print(Linear_Search([12,45,78,69,32],32)) 