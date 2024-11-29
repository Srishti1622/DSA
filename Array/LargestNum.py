# Find the largest element in the given array

# 1st Approach:
def WayOne(arr):
    arr.sort()
    return arr[len(arr)-1]

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr.copy())
print("Largest element in given array using 1st approach is ",res1)