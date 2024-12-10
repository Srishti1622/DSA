# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 6a: Inverted Star Pyramid-i
print('--------------------------------')
print('Inverted Star Pyramid-i')
for i in range(n,0,-1):
    k=0
    for j in range(2*i-1):
        while(n-i>k):
           k+=1
           print(' ',end=' ')
        print('*',end=' ')
    print('\n')

# pattern 6b: Inverted Star Pyramid-ii
print('--------------------------------')
print('Inverted Star Pyramid-ii')
for i in range(n,0,-1):
    k=0
    for j in range(2*i-1):
        while(n-i>k):
           k+=1
           print(' ',end=' ')
        print(i,end=' ')
    print('\n')

# pattern 6c: Inverted Star Pyramid-iii
print('--------------------------------')
print('Inverted Star Pyramid-iii')
for i in range(n,0,-1):
    k=0
    breakpoint=(2*i-1)/2
    point=0
    for j in range(2*i-1):
        while(n-i>k):
           k+=1
           print(' ',end=' ')
        if j<=breakpoint:
            point+=1
        else:
            point-=1
        print(point,end=' ')
    print('\n')

# pattern 6d: Alpha Inverted Star Pyramid-iv
print('--------------------------------')
print('Alpha Star Inverted Pyramid-iv')
for i in range(n,0,-1):
    k=0
    breakpoint=(2*i-1)//2
    point='A'
    while(n-i>k):
        k+=1
        print(' ',end=' ')
    for j in range(2*i-1):
        print(point,end=' ')
        if j<breakpoint:
            point=chr(ord(point)+1)
        else:
            point=chr(ord(point)-1)
    print('\n')

