# Given an array of N integers, write a program to implement the Selection sorting algorithm.

# select the minimun element from the unsorted array and swap - first the smallest element will get sorted

# Reference: https://www.geeksforgeeks.org/problems/selection-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=selection-sort

def SelectionSort(arr):
    for i in range(len(arr)-1):
        mini=i
        for j in range(i+1,len(arr)):
            if arr[mini]>arr[j]:
                mini=j
        temp=arr[mini]
        arr[mini]=arr[i]
        arr[i]=temp
    return arr
            

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=SelectionSort(arr.copy())
print("Selection sorting given array is ",res1)