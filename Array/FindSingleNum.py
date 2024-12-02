# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

# Reference: https://leetcode.com/problems/single-number/description/

# 1st Approach:
def WayOne(arr):
    for i in range(len(arr)):
        flag=0
        for j in range(len(arr)):
            if arr[j]==arr[i]:
                flag+=1
        if flag==1:
            return arr[i]
    return -1

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr)
print("Element that appears once in given array using 1st approach is ",res1)