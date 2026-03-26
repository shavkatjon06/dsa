# Given two arrays a[] and b[] of size m and n respectively, the task is to determine
# whether b[] is a subset of a[]. Both arrays are not sorted, and elements are distinct.


def isSubset(list1, list2):
    bag = {}
    for i in list1:
        bag[i] = True
    for i in list2:
        if i not in bag:
            return False
    return True


print(isSubset([1, 2, 3, 4, 5, 6], [1, 2, 4]))
print(isSubset([10, 5, 2, 23, 19], [19, 5, 3]))
