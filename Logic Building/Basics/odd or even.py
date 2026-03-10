# Given a number n, check whether it is even or odd. Return true for even and false for odd.

def isEven(number):
    remainder = number % 2
    if remainder == 0:
        return True
    else:
        return False

n = 15
print(isEven(n))
n=10
print(isEven(n))