# Given an array arr[] of size n, the task is to find all the Leaders in
# the array. An element is a Leader if it is greater than or equal to all
# the elements to its right side.

# Note: The rightmost element is always a leader.


def leader(list):
    res = []
    for i in range(len(list)):
        isLeader = True
        for x in range(i+1, len(list)):
            if list[i] < list[x]:
                isLeader = False
                break
        if isLeader:
            res.append(list[i])
    return res


print(leader([16, 17, 4, 3, 5, 2]))
