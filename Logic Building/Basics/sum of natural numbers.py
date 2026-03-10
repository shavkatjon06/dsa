# Given a positive integer n, find the sum of the first n natural numbers.

# using loop
def sum1(number):
    result = 0
    for i in range(1, number+1):
        result += i
    return result


print(sum1(3))
