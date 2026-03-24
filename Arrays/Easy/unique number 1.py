# Given an array of integers, every element in the array appears twice except for one
# element which appears only once. The task is to identify and return the element that
# occurs only once.


def uniqueNum(list):
    bag = {}
    for i in list:
        if i in bag:
            bag[i] += 1
        else:
            bag[i] = 1
    for key, value in bag.items():
        if value == 1:
            return key
    return None


print(uniqueNum([2, 3, 5, 4, 5, 3, 4]))
