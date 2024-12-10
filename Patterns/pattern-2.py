# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 2a: Right-Angled Triangle Pattern-i
print('--------------------------------')
print('Right-Angled Triangle Pattern-i')
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print('\n')

# pattern 2b: Left-Angled Triangle Pattern-i
print('--------------------------------')
print('Left-Angled Triangle Pattern-i')
for i in range(1,n+1):
    k=0
    for j in range(i):
        while(n-i>k):
            k+=1
            print(' ',end=' ')
        print('*',end=' ')
    print('\n')

# pattern 2c: Right-Angled Triangle Pattern-ii
print('--------------------------------')
print('Right-Angled Triangle Pattern-ii')
point=1
for i in range(1,n+1):
    for j in range(i):
        print(point,end=' ')
        point+=1
    print('\n')

# pattern 2d: Right-Angled Triangle Pattern-iii
print('--------------------------------')
print('Right-Angled Triangle Pattern-iii')
point='A'
for i in range(1,n+1):
    for j in range(i):
        print(point,end=' ')
        point=chr(ord(point)+1)
    print('\n')

# pattern 2e: Right-Angled Triangle Pattern-iv
print('--------------------------------')
print('Right-Angled Triangle Pattern-iv')
for i in range(1,n+1):
    point='A'
    for j in range(i):
        print(point,end=' ')
        point=chr(ord(point)+1)
    print('\n')

# pattern 2f: Right-Angled Triangle Pattern-v
print('--------------------------------')
print('Right-Angled Triangle Pattern-v')
point='A'
for i in range(1,n+1):
    for j in range(i):
        print(point,end=' ')
    point=chr(ord(point)+1)
    print('\n')

# pattern 2g: Right-Angled Triangle Pattern-vi
print('--------------------------------')
print('Right-Angled Triangle Pattern-vi')
for i in range(n):
    for j in range(ord('A') + n - 1 - i, ord('A') + n):
        print(chr(j),end=' ')
    print('\n')

# pattern 2h: Right-Angled Triangle Pattern-vii having only 1 and 0
print('--------------------------------')
print('Right-Angled Triangle Pattern-vii having only 1 and 0')
for i in range(1,n+1):
    point=1
    if i%2==0:
        point=0
    for j in range(i):
        print(point,end=' ')
        point=1 if point==0 else 0
    print('\n')