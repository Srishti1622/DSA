# Check if the geiven array is sorted or not

# 1st Approach:
def WayOne(arr1,arr2):
    arr2.sort()
    return arr1==arr2

# 2nd Approach: Optimized
def WayTwo(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
    return True

# 3rd Approach: Naive
def WayThree(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                return False
    return True

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr,arr.copy())
print("Checking given array is sorted or not using 1st approach is ",res1)
# 2nd way of doing it
res2=WayTwo(arr)
print("Checking given array is sorted or not using 2nd approach is ",res2)
# 3rd way of doing it
res3=WayThree(arr)
print("Checking given array is sorted or not using 3rd approach is ",res3)