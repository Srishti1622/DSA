# Given an integer N, return the number of digits in N.

# Reference: 

import math

# 1st Approach: Brute-force
def WayOne(num):
    str_num=str(num)
    return len(str_num)

# 2nd Approach: Brute-force
def WayTwo(num):
    count=0
    while(num>0):
        count+=1
        num=num//10
    return count

# 3rd Approach: Optimized
def WayThree(num):
    return int(math.log10(num)+1)

# getting the number from user
num=int(input("Enter the number: "))
# 1st way of doing this
res1=WayOne(num)
print(f"The length of given number using 1st way is : {res1}")
# 2nd way of doing this
res2=WayTwo(num)
print(f"The length of given number using 2nd way is : {res2}")
# 3rd way of doing this
res3=WayThree(num)
print(f"The length of given number using 3rd way is : {res3}")