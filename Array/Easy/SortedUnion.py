# Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

# Reference: https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays

# 1st Approach: Works with both sorted or unsorted array
def WayOne(arr1, arr2):
    s = set()
    union = []
    for num in arr1:
        s.add(num)
    for num in arr2:
        s.add(num)
    for num in s:
        union.append(num)
    union.sort()
    return union

# 2nd Approach: works only with sorted arrays
def WayTwo(arr1, arr2):
    new_arr=[]
    i=0
    j=0
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<=arr2[j]:
            if len(new_arr)==0 or new_arr[-1]!=arr1[i]:
                new_arr.append(arr1[i])
            i=i+1
        else:
            if len(new_arr)==0 or new_arr[-1]!=arr2[j]:
                new_arr.append(arr2[j])
            j=j+1
    while i < len(arr1): 
        if new_arr[-1] != arr1[i]:
            new_arr.append(arr1[i])
        i += 1
    while j < len(arr2): 
        if new_arr[-1] != arr2[j]:
            new_arr.append(arr2[j])
        j += 1
    return new_arr

# getting 1st array size and elements from user
arr1=[]
n=int(input("Enter the length of 1st array: "))
for i in range(n):
    arr1.append(int(input("Enter 1st array element: ")))

print("Array you provided: ",arr1)

# getting 2nd array size and elements from user
arr2=[]
n=int(input("Enter the length of 2nd array: "))
for i in range(n):
    arr2.append(int(input("Enter 2nd array element: ")))

print("Array you provided: ",arr2)
# 1st way of doing it
res1=WayOne(arr1.copy(),arr2.copy())
print("Union of two sorted array using 1st approach is ",res1)
# 2nd way of doing it
res2=WayTwo(arr1.copy(),arr2.copy())
print("Union of two sorted array using 2nd approach is ",res2)