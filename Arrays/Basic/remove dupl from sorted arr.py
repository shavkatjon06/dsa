# Given a sorted array arr[] of size n, the goal is to rearrange the array so that
# all distinct elements appear at the beginning in sorted order. Additionally, return
# the length of this distinct sorted subarray.


def removeDupl1(list):
    bag = {}
    res = []
    for i in range(len(list)-1):
        if list[i] not in bag:
            bag[list[i]] = True
    for key in bag.keys():
        res.append(key)
    return res


print(removeDupl1([2, 2, 2, 2]))
print(removeDupl1([1, 2, 2, 3, 4, 4, 5, 5]))


def removeDupl2(list):
    bag = set()
    index = 0
    for i in range(len(list)):
        if list[i] not in bag:
            bag.add(list[i])
            list[index] = list[i]
            index += 1
    return list[0:index]


print(removeDupl2([2, 2, 2, 2]))
print(removeDupl2([1, 2, 2, 3, 4, 4, 5, 5]))


def removeDupls3(list):
    idx = 1
    for i in range(1, len(list)):
        if list[i] != list[i-1]:
            list[idx] = list[i]
            idx += 1
    return list[0:idx]


print(removeDupls3([2, 2, 2]))
print(removeDupls3([1, 2, 2, 3, 4, 4, 5, 5]))
