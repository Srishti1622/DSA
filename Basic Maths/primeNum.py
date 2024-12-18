# Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

# Reference:

import math

# 1st Approach: Brute-force
def WayOne(num):
    flag=0
    if num==0 or num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            flag=1
        if flag==1:
            return False
    return True

# 2nd Approach: Optimized
def WayTwo(num):
    flag=0
    if num==0 or num==1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

# getting number from user
num=int(input("Enter number to be checked: "))
# 1st way of doing it
res1=WayOne(num)
print(f"The given number is prime or not using 1st approach: {res1}")
# 2nd way of doing it
res2=WayTwo(num)
print(f"The given number is prime or not using 2nd approach: {res2}")