# Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

# Reference: 

# 1st Approach:
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