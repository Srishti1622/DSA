# Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

# Reference: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k

# 1st Approach: Burte-force
def WayOne(arr,k):
    length=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            s=0
            for kk in range(i,j+1):
                s=s+arr[kk]
            if s==k:
                length=max(length,j-i+1)
    return length

# 2nd Approach: Better Burte-force
def WayTwo(arr,k):
    length=0
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s=s+arr[j]
            if s==k:
                length=max(length,j-i+1)
    return length

# 3rd Approach: Better one for positive arrays and optimized for positive/negative arrays
def WayThree(arr,k):
    preSumMap={}
    Sum=0
    maxLen=0
    for i in range(n):
        Sum += arr[i]
        if Sum == k:
            maxLen = max(maxLen, i + 1)
        rem = Sum - k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)
        if Sum not in preSumMap:
            preSumMap[Sum] = i
    return maxLen

# 4th Approach: Optimized
def WayFour(arr,k):
    maxLen=0
    left=0
    right=0
    Sum=arr[0]
    while(right<len(arr)):
        while left <= right and Sum > k:
            Sum -= arr[left]
            left += 1
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)
        right += 1
        if right < n: Sum += arr[right]
    return maxLen

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
# 2nd way of doing it
res2=WayTwo(arr,k)
print(f"Longest sybarray with sum {k} using 2nd approach is ",res2)
# 3rd way of doing it
res3=WayThree(arr,k)
print(f"Longest sybarray with sum {k} using 3rd approach is ",res3)
# 4th way of doing it
res4=WayFour(arr,k)
print(f"Longest sybarray with sum {k} using 4th approach is ",res4)