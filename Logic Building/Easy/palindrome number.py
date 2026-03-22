# Given an integer n, determine whether it is a palindrome number or not.
# A number is called a palindrome if it reads the same from forward and backward.


def palindrome(n):
    n = str(n)
    length = len(n)-1
    for i in range(length // 2):
        if n[i] != n[length-i]:
            return False
    return True


print(palindrome(12321))
