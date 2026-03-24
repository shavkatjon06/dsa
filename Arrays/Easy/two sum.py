# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.


def twoSum1(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return [i, j]
    return None


print(twoSum1([2, 7, 11, 15], 9))


def twoSum2(list, target):
    bag = {}
    for idx, val in enumerate(list):
        difference = target - val
        if difference in bag:
            return [idx, bag[difference]]
        bag[val] = idx
    return None


print(twoSum2([2, 7, 11, 15], 9))
