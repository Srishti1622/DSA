# Remove duplicate in-place elements from sorted array

# 1st Approach:
def WayOne(arr):
    return set(arr)

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr.copy())
print("Remove duplicate element in given sorted array using 1st approach is ",res1)