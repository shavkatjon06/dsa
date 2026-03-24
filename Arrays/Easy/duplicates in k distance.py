# Given an integer array arr[] and an integer k, determine whether there
# exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k.
# If such a pair exists, return 'Yes', otherwise return 'No'.

def kDistance(list, k):
    bag = {}
    for idx, val in enumerate(list):
        if val in bag:
            if idx - bag[val] <= k:
                return 'Yes'
        else:
            bag[val] = idx
    return 'No'


print(kDistance([1, 2, 3, 4, 1, 2, 3, 4], 3))
print(kDistance([1, 2, 3, 1, 4, 5], 3))
