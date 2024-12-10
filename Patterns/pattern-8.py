# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 8a: half Diamond Shape
print('--------------------------------')
print('half Diamond Shape')
for i in range(1,n):
    for j in range(i):
        print('*',end=' ')
    print('\n')
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print('\n')