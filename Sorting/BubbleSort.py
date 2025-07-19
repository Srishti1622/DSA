# Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

# push the max element at the last by adjacent swapping - in this algo, array get sorted by max to min which means the largest element in the array get placed first in the last index of array 

# Reference: https://www.geeksforgeeks.org/problems/bubble-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bubble-sort

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr

def OptimizedBubbleSort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                swapped=True
        if not swapped:
            break
    return arr

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=BubbleSort(arr.copy())
print("Bubble sorting given array is ",res1)

# 2nd way - optimized O(n) when array is already sorted
res2=OptimizedBubbleSort(arr.copy())
print("Optimized Bubble sorting given array is ",res2)