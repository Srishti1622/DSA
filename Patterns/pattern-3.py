# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 3a: Right-Angled Number Pyramid-i
print('--------------------------------')
print('Right-Angled Number Pyramid-i')
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=' ')
    print('\n')

# pattern 3b: Right-Angled Number Pyramid-ii
print('--------------------------------')
print('Right-Angled Number Pyramid-ii')
for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
    print('\n')

# pattern 3c: Left-Angled Number Pyramid-i
print('--------------------------------')
print('Left-Angled Number Pyramid-i')
for i in range(1,n+1):
    k=0
    for j in range(i):
        while(n-i>k):
            k+=1
            print(' ',end=' ')
        print(j+1,end=' ')
    print('\n')

# pattern 3d: Left-Angled Number Pyramid-ii
print('--------------------------------')
print('Left-Angled Number Pyramid-ii')
for i in range(1,n+1):
    k=0
    for j in range(i):
        while(n-i>k):
            k+=1
            print(' ',end=' ')
        print(i,end=' ')
    print('\n')