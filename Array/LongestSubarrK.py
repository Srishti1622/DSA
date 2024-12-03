# Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

# Reference: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k

# 1st Approach: Burte-force
def WayOne(arr,k):
    length=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            s=0
            for kk in range(i,j+1):
                s=s+arr[kk]
            if s==k:
                length=max(length,j-i+1)
    return length

# getting array size and elements from user
arr=[]
k=int(input("Enter the sum: "))
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr,k)
print(f"Longest sybarray with sum {k} using 1st approach is ",res1)