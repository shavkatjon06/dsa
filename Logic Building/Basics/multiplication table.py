# Given a number n, we need to print its table.

# iterative approach
def table(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")


table(5)


# recursive approach
def table2(number, i=1):
    if i >= 11:  # when it becomes 11, our recursion stops
        return
    print(f"{number} * {i} = {number * i}")  # we multiply 2*1, 2*2, 2*3
    i += 1  # as we increase our i in each function call after each print
    table2(number, i)  # then call our function


table2(2)
