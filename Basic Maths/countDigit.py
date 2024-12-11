# Given an integer N, return the number of digits in N.

# Reference: 

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

# getting the number from user
num=int(input("Enter the number: "))
# 1st way of doing this
res1=WayOne(num)
print(f"The length of given number is : {res1}")
# 2nd way of doing this
res2=WayTwo(num)
print(f"The length of given number is : {res2}")