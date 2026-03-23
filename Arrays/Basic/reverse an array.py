# Reverse an array arr[]. Reversing an array means rearranging the elements such that
# the first element becomes the last, the second element becomes second last and so on.

def reverse1(list):
    temp = []
    for i in range(len(list)):
        temp.append(list.pop())
    return temp


print(reverse1([1, 2, 3, 4]))


def reverse2(list):
    first = 0
    last = len(list)-1
    while first < last:
        list[first], list[last] = list[last], list[first]
        first += 1
        last -= 1
    return list


print(reverse2([1, 2, 3, 4]))
