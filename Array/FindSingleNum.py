# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

# Reference: https://leetcode.com/problems/single-number/description/

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr)
print("Maximum Consecutive ones in given array using 1st approach is ",res1)