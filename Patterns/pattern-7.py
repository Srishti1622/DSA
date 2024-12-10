# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 7a: Diamond Shape
print('--------------------------------')
print('Diamond Shape')
for i in range(n):
    k=0
    for j in range(2*i+1):
        while(n-i-1>k):
           k+=1
           print(' ',end=' ')
        print('*',end=' ')
    print('\n')
for i in range(n,0,-1):
    k=0
    for j in range(2*i-1):
        while(n-i>k):
           k+=1
           print(' ',end=' ')
        print('*',end=' ')
    print('\n')