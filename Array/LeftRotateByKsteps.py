# Given an integer array nums and a non-negative integer k, rotate the array to left by k steps


# 1st Approach:
def WayOne(arr,k):
    temp=0
    for i in range(k):
        temp=arr[0]
        for j in range(1,len(arr)):
            arr[j-1]=arr[j]
        arr[len(arr)-1]=temp
    return arr

# getting array size and elements from user
arr=[]
k=int(input("Enter the k step value to rotate: "))
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("K steps: ",k)
print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr,k)
print(f"Array after {k} rotates: {res1}")