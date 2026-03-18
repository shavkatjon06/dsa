# Gevin two numbers a and b, the task is to swap them

# first approach
def swap1(a, b):
    temp = a
    a = b
    b = temp
    del temp
    return a, b


print(swap1(3,4))

# 2nd approach
def swap2(a, b):
    a, b = b, a
    return a, b


print(swap2(2, 5))