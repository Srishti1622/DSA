# Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

# Reference: https://leetcode.com/problems/max-consecutive-ones/description/

# 1st Approach:
def WayOne(arr):
    count=0
    c=0
    for i in arr:
        if i==1:
            count+=1
        else:
            count=0
        c=max(c,count)
    return c

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr)
print("Maximum Consecutive ones in given array using 1st approach is ",res1)