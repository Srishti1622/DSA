# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 1: butterfly shape
print('--------------------------------')
print('butterfly shape')
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=' ')
    for j in range(2*(n-i)):
        print(' ',end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    print('\n')
for i in range(n-1,0,-1):
    for j in range(i):
        print(j+1,end=' ')
    for j in range(2*(n-i)):
        print(' ',end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    print('\n')