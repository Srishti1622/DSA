# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 4a: Inverted Right Pyramid-i
print('--------------------------------')
print('Inverted Right Pyramid-i')
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print('\n')

# pattern 4b: Inverted Right Pyramid-ii
print('--------------------------------')
print('Inverted Right Pyramid-ii')
for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end=' ')
    print('\n')

# pattern 4c: Inverted Left Pyramid-i
print('--------------------------------')
print('Inverted Left Pyramid-i')
for i in range(n,0,-1):
    k=0
    for j in range(i):
        while(n-i>k):
           k+=1
           print(' ',end=' ')
        print('*',end=' ')
    print('\n')

# pattern 4d: Inverted Left Pyramid-ii
print('--------------------------------')
print('Inverted Left Pyramid-ii')
for i in range(n,0,-1):
    k=0
    for j in range(i):
        while(n-i>k):
           k+=1
           print(' ',end=' ')
        print(j+1,end=' ')
    print('\n')
