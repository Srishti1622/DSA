# Given an array of integers nums, return the 2nd-largest element in the array. If the 2nd-largest element does not exist, return -1

# Reference: https://www.geeksforgeeks.org/problems/second-largest3735/1

# 1st Approach: Using set and sort
def WayOne(arr):
    arr=list(set(arr))
    arr.sort()
    if len(arr)<=1:
        return -1
    return arr[len(arr)-2]

# 2nd Approach: Using sort only
def WayTwo(arr):
    arr.sort()
    for i in range(len(arr),0,-1):
        if arr[i-1]!=arr[i-2]:
            return arr[i-2]
    return -1

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr)
print("Second-Largest element in given array using 1st approach is ",res1)
# 2nd way of doing it
res2=WayTwo(arr)
print("Second-Largest element in given array using 2nd approach is ",res2)

