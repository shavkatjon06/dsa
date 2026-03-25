# Given an integer array nums and an integer val, remove all
# occurrences of val in nums in-place


def removeElement(list, val):
    k = 0
    for i in range(len(list)):
        if list[i] != val:
            list[k] = list[i]
            k += 1
    return list[0:k], k


print(removeElement([0,1,2,2,3,0,4,2], 2))
