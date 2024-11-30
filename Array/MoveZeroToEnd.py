# Given an array of integers arr[], the task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

# Reference: https://leetcode.com/problems/move-zeroes/description/

# 1st Approach: Burte force
def WayOne(arr):
    new_arr=[]
    for i in range(len(arr)):
        if arr[i]!=0:
            new_arr.append(arr[i])
    while(len(new_arr)!=len(arr)):
        new_arr.append(0)
    return new_arr

# 2nd Approach: Burte force
def WayTwo(arr):
    temp=[]
    for i in range(len(arr)):
        if arr[i]!=0:
            temp.append(arr[i])
    for i in range(len(temp)):
        arr[i]=temp[i]
    for i in range(len(temp),len(arr)):
        arr[i]=0  
    return arr

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr.copy())
print("Move Zero to end using 1st approach is ",res1)
# 2nd way of doing it
res2=WayTwo(arr.copy())
print("Move Zero to end using 2nd approach is ",res2)