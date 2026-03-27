# Given an array arr[], the task is to find the maximum distance between two
# occurrences of any element. If no element occurs twice, return 0.


def maxDiff(list):
    bag = {}
    res = 0
    for idx, val in enumerate(list):
        if val in bag:
            diff = idx - bag[val]
            if diff > res:
                res = diff
        else:
            bag[val] = idx
    return res


print(maxDiff([1, 1, 2, 2, 2, 1]))
print(maxDiff([1, 2, 3, 6, 5, 4]))
