# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 2a: Right-Angled Triangle Pattern
print('--------------------------------')
print('Right-Angled Triangle Pattern')
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print('\n')

# pattern 2b: Left-Angled Triangle Pattern
print('--------------------------------')
print('Left-Angled Triangle Pattern')
for i in range(1,n+1):
    k=0
    for j in range(i):
        while(n-i>k):
            k+=1
            print(' ',end=' ')
        print('*',end=' ')
    print('\n')