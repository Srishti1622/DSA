# Check if the geiven array is sorted or not

# 1st Approach:
def WayOne(arr1,arr2):
    arr2.sort()
    return arr1==arr2

# getting array size and elements from user
arr=[]
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr,arr.copy())
print("Checking given array is sorted or not using 1st approach is ",res1)