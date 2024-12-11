# Given an integer N return the reverse of the given number.
# Note: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

# Reference: 

import math

# 1st Approach: Brute-force


# getting the number from user
num=int(input("Enter the number: "))
# 1st way of doing this
res1=WayOne(num)
print(f"The length of given number using 1st way is : {res1}")