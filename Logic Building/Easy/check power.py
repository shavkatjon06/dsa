# Given two positive numbers x and y, check if y is a power of x or not.

def checkPower(a, b):
    if b == 1:
        return True
    if a == 1:
        return b == 1
    power = 1
    while power < b:
        power = power * a
    return  power == b


print(checkPower(10, 1000))
print(checkPower(3, 10))

# logx(y) = log(y) / log(x)