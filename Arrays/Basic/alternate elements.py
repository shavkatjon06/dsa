# Given an array arr[], the task is to print every alternate element of
# the array starting from the first element.


def alternates(list):
    length = len(list)
    res = []
    for i in range(0, length, 2):
        res.append(list[i])
    return res


print(alternates([1, 2, 3, 4, 5, 6]))
