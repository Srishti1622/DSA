# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

# Reference: https://leetcode.com/problems/single-number/description/

# 1st Approach: Brute-force
def WayOne(arr):
    for i in range(len(arr)):
        flag=0
        for j in range(len(arr)):
            if arr[j]==arr[i]:
                flag+=1
        if flag==1:
            return arr[i]
    return -1

# 2nd Approach: Optimized 
# as per xor property, xor of same number is 0
def WayTwo(arr):
    xor=0
    for i in range(len(arr)):
        xor=arr[i]^xor
    return xor

# 3rd Approach: Better but it will cause issue when arr have negative elements
def WayThree(arr):
    maxi=max(arr)
    map_arr=[0]*(maxi+1)
    for i in range(len(arr)):
        map_arr[arr[i]]+=1
    for i in arr:
        if map_arr[i]==1:
            return i
    return -1

# 4th Approach: same as 3rd using inbuild hashmap method 
def WayFour(arr):
    hashmap={}
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1
    for num, count in hashmap.items():
        if count == 1:
            return num
    return -1

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr)
print("Element that appears once in given array using 1st approach is ",res1)
# 2nd way of doing it
res2=WayTwo(arr)
print("Element that appears once in given array using 2nd approach is ",res2)
# 3rd way of doing it
res3=WayThree(arr)
print("Element that appears once in given positive array using 3rd approach is ",res3)
# 4th way of doing it
res4=WayFour(arr)
print("Element that appears once in given positive array using 4th approach is ",res4)