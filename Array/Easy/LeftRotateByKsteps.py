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

# 2nd Approach:
def WayTwo(arr,k):
    temp=[]
    new_arr=[]
    k=k%len(arr)
    for i in range(k):
        temp.append(arr[i])
    for i in range(k,len(arr)):
        new_arr.append(arr[i])
    for i in range(len(temp)):
        new_arr.append(temp[i])
    return new_arr

# 3rd Approach:
def WayThree(arr,k):
    k=k%len(arr)
    # to reverse the array of size k from starting
    i=0
    j=k-1
    while(i<j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i=i+1
        j=j-1
    # to reverse the array from k to end
    i=k
    n=len(arr)-1
    while(i<n):
        temp=arr[i]
        arr[i]=arr[n]
        arr[n]=temp
        i=i+1
        n=n-1
    # to reverse the entire array
    i=0
    n=len(arr)-1
    while(i<n):
        temp=arr[i]
        arr[i]=arr[n]
        arr[n]=temp
        i=i+1
        n=n-1
    return arr

# 4th Approach:
def WayFour(arr,k):
    new_arr=arr.copy()
    for i in range(len(arr)):
        if i<k:
            new_arr[len(arr)-k+i]=arr[i]
        else:
            new_arr[i-k]=arr[i]
    return new_arr

# getting array size and elements from user
arr=[]
k=int(input("Enter the k step value to rotate: "))
n=int(input("Enter the length of array: "))
for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("K steps: ",k)
print("Array you provided: ",arr)
# 1st way of doing it
res1=WayOne(arr.copy(),k)
print(f"Array after {k} rotates using 1st way: {res1}")
# 2nd way of doing it
res2=WayTwo(arr.copy(),k)
print(f"Array after {k} rotates using 2nd way: {res2}")
# 3rd way of doing it
res3=WayThree(arr.copy(),k)
print(f"Array after {k} rotates using 3rd way: {res3}")
# 4th way of doing it
res4=WayFour(arr.copy(),k)
print(f"Array after {k} rotates using 4th way: {res4}")