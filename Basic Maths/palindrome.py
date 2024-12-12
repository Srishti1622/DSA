# Given an integer N, return true if it is a palindrome else return false.
# Note: A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

# Reference:

# 1st Approach: 
def WayOne(num):
    num1=int(''.join(reversed(str(num))))
    return num==num1

# getting number from user
num=int(input("Enter number to be checked: "))
# 1st way of doing it
res1=WayOne(num)
print(f"The given number is palidrome or not: {res1}")