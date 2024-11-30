# Remove duplicate in-place elements from sorted array

# Reference: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# 1st Approach:
def WayOne(arr):
    return list(set(arr))

# 2nd Approach:
def WayTwo(arr):
    new_arr=[arr[0]]
    j=1
    for i in range(len(arr)-1):
        if arr[i]!=arr[j] and arr[j] not in new_arr:
            new_arr.append(arr[j])
        j+=1
    return new_arr

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr.copy())
print("Remove duplicate element in given sorted array using 1st approach is ",res1)
# 2nd way of doing it
res2=WayTwo(arr.copy())
print("Remove duplicate element in given sorted array using 2nd approach is ",res2)