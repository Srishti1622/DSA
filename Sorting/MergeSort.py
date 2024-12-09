# Given an array of size n, sort the array using Merge Sort.

# Reference: https://www.geeksforgeeks.org/problems/merge-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=merge-sort

# Explain: merge sort is a divide and merge (conquers algorithm), it divides the array hypothetically in two parts until each sub-array becomes of length 1 and then merge each in sorted form

def MergeSort(arr):
    low=0
    high=len(arr)-1
    mid=int(len(arr)/2)-1
    if len(arr)%2!=0:
        mid=mid+1
    print(low,mid,mid+1,high)


# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=MergeSort(arr.copy())
print("Merge sorting given array is ",res1)