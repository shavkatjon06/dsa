# Given an integer n, for every positive integer i <= n, the task is to pring,

# "FizzBuzz" if i is divisible by 3 and 5,
# "Fizz" if i is divisible by 3,
# "Buzz" if i is divisible by 5
# "i" as a string, if none of the conditions are true.


def fizzBuzz(n):
    res = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(f"{i}")
    return res


print(fizzBuzz(16))
