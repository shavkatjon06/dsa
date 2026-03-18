# Given an Integer n, find the reverse of its digits.

def reverseDigit(x):
    sign = -1 if x < 0 else 1
    x = str(abs(x))  # abs, non-negative
    result = ""
    for i in range(len(x)-1, -1, -1):
        result += x[i]
    return int(result) * sign


print(reverseDigit(123))
print(reverseDigit(-123))
