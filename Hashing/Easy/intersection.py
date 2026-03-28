# Given two arrays a[] and b[], find their intersection — the unique elements that
# appear in both. Ignore duplicates, and the result can be in any order.


def intersection1(list1, list2):
    res = []
    for i in list1:
        for j in list2:
            if i == j and i not in res:
                res.append(i)
    return res


print(intersection1([1, 2, 1, 3, 1], [3, 1, 3, 4, 1]))
print(intersection1([1, 2, 3], [4, 5, 6]))


def intersection2(list1, list2):
    bag = {}
    bag2 = {}
    temp = []
    for i in list1:
        if i not in bag:
            bag[i] = True
    for i in list2:
        if i in bag and i not in bag2:
            temp.append(i)
            bag2[i] = True
    return temp


print(intersection2([1, 2, 1, 3, 1], [3, 1, 3, 4, 1]))
print(intersection2([1, 2, 3], [4, 5, 6]))