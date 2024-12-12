# Given an integer N return the reverse of the given number.
# Note: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

# Reference: 

import math

# 1st Approach: Brute-force
def WayOne(num):
    str_num=str(num)
    r_reverse=''.join(reversed(str_num))
    return int(r_reverse)

# 2nd Approach: Brute-force
def WayTwo(num):
    r_reverse=0
    while(num>0):
        rem=num%10
        r_reverse=r_reverse*10+rem
        num=num//10
    return r_reverse

# getting the number from user
num=int(input("Enter the number: "))
# 1st way of doing this
res1=WayOne(num)
print(f"The length of given number using 1st way is : {res1}")
# 2nd way of doing this
res2=WayTwo(num)
print(f"The length of given number using 2nd way is : {res2}")