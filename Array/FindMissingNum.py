# Given an array arr[] of size n-1 with integers in the range of [1, n], the task is to find the missing number from the first N integers.
# Note: There are no duplicates in the list.

# Reference: https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

# 1st Approach:
def WayOne(arr):
    n=len(arr)+1
    sum_arr=sum(arr)
    formula=(n*(n+1))/2
    return int(formula-sum_arr)

# 2nd Approach:
def WayTwo(arr):
    xor1=0
    xor2=0
    for num in arr:
        xor1^=num
    for i in range(1,len(arr)+2):
        xor2^=i
    return xor1^xor2

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr.copy())
print("Missing element in given array using 1st approach is ",res1)
# 2nd way of doing it
res2=WayTwo(arr.copy())
print("Missing element in given array using 2nd approach is ",res2)