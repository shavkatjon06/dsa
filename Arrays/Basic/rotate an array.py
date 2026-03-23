# left rotation

def leftRotation(list, d):
    length = len(list)
    for _ in range(d):
        first = list[0]
        for i in range(length-1):
            list[i] = list[i+1]
        list[-1] = first
    return list


print(leftRotation([1, 2, 3, 4, 5, 6], 2))


# right rotation

def rightRotation(list, d):
    length = len(list) - 1
    for _ in range(d):
        last = list[-1]
        for i in range(length, 0, -1):
            list[i] = list[i-1]
        list[0] = last
    return list


print(rightRotation([1, 2, 3, 4, 5, 6], 2))