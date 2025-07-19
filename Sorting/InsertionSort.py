# Given an array of N integers, write a program to implement the Insertion sorting algorithm.

# take an element and place it in it's correct position - will compare the current index element with it's previous index element

# Reference: https://www.geeksforgeeks.org/problems/insertion-sort/0?category%5B%5D=Algorithms&page=1&query=category%5B%5DAlgorithmspage1&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=insertion-sort

def InsertionSort(arr):
    for i in range(len(arr)):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            temp=arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=temp
            j-=1
    return arr

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=InsertionSort(arr.copy())
print("Insertion sorting given array is ",res1)