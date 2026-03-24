# Given an array of integers arr[], move all the zeros to the end of the array
# while maintaining the relative order of all non-zero elements.
from django.template.defaultfilters import length


def zeroesToEnd1(list):
    length = len(list)
    temp = [0] * length
    idx = 0
    for i in range(length):
        if list[i] != 0:
            temp[idx] = list[i]
            idx += 1
    return temp


print(zeroesToEnd1([1, 0, 2, 3, 0, 0, 4]))


def zeroesToEnd2(list):
    idx = 0
    for i in list:
        if i != 0:
            list[idx] = i
            idx += 1
    while idx < len(list):
        list[idx] = 0
        idx += 1
    return list


print(zeroesToEnd2([1, 0, 2, 3, 0, 0, 4]))