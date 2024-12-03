# Given an array and a num which we need to find whether the num is present in the array or not if present then return the index else return -1

# Reference: https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win

# 1st Approach: When array must be in sorted order
def WayOne(arr,num):
    for i in arr:
        if i>num:
            return False
        elif i==num:
            return True
    return False

# 2nd Approach: Return index if the num is present
def WayTwo(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1

# getting array size and elements from user
arr=[]
num=int(input("Enter num to be searched: "))
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
print("Number to be searched: ",num)
# 1st way of doing it
res1=WayOne(arr.copy(),num)
print(f"Finding {num} in given array when must be in sorted order using 1st approach is ",res1)
# 1st way of doing it
res2=WayTwo(arr.copy(),num)
print(f"Finding {num} index in given array using 2nd approach is ",res2)