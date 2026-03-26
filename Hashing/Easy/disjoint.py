# Given two arrays a[] and b[], check if they are disjoint, i.e., there is no element
# common between both the arrays.


def disjoint(list1, list2):
    bag = {}
    for i in list1:
        bag[i] = True
    for i in list2:
        if i in bag:
            return False
    return True


print(disjoint([12, 34, 11, 9], [2, 1, 3, 5]))
print(disjoint([12, 34, 11, 9, 3], [2, 1, 3, 5]))