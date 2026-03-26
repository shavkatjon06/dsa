# Given two arrays, a[] and b[] of equal length. The task is to
# determine if the given arrays are equal or not. Two arrays are considered equal if:
# Both arrays contain the same set of elements.
# The arrangements (or permutations) of elements may be different.
# If there are repeated elements, the counts of each element must be the same in both arrays.


def equals(list1, list2):
    if len(list1) != len(list2):
        return False
    bag = {}
    for i in list1:
        if i in bag:
            bag[i] += 1
        else:
            bag[i] = 1
    for i in list2:
        if i not in bag:
            return False
        if bag[i] == 0:
            return False
        bag[i] -= 1
    return True


print(equals([1, 2, 5, 4, 0], [2, 4, 5, 0, 1]))
print(equals([1, 1, 7], [1, 7, 7]))
