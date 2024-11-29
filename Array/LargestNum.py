# Find the largest element in the given array

# Reference: https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array

# 1st Approach:
def WayOne(arr):
    arr.sort()
    return arr[len(arr)-1]

# 2nd Approach:
def WayTwo(arr):
    large=0
    for i in range(len(arr)):
        if arr[i]>large:
            large=arr[i]
    return large

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr.copy())
print("Largest element in given array using 1st approach is ",res1)
# 2nd way of doing it
res2=WayTwo(arr.copy())
print("Largest element in given array using 2nd approach is ",res2)