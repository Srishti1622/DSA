# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 5a: Star Pyramid-i
print('--------------------------------')
print('Star Pyramid-i')
for i in range(n):
    k=0
    for j in range(2*i+1):
        while(n-i-1>k):
           k+=1
           print(' ',end=' ')
        print('*',end=' ')
    print('\n')

# pattern 5b: Star Pyramid-ii
print('--------------------------------')
print('Star Pyramid-ii')
for i in range(n):
    k=0
    for j in range(2*i+1):
        while(n-i-1>k):
           k+=1
           print(' ',end=' ')
        print(i+1,end=' ')
    print('\n')

# pattern 5c: Star Pyramid-iii
print('--------------------------------')
print('Star Pyramid-iii')
for i in range(n):
    k=0
    breakpoint=(2*i+1)/2
    point=0
    for j in range(2*i+1):
        while(n-i-1>k):
           k+=1
           print(' ',end=' ')
        if j<=breakpoint:
            point+=1
        else:
            point-=1
        print(point,end=' ')
    print('\n')

# pattern 5d: Alpha Star Pyramid-iv
print('--------------------------------')
print('Star Pyramid-iv')
for i in range(n):
    k=0
    breakpoint=(2*i+1)//2
    point='A'
    while(n-i-1>k):
        k+=1
        print(' ',end=' ')
    for j in range(2*i+1):
        print(point,end=' ')
        if j<breakpoint:
            point=chr(ord(point)+1)
        else:
            point=chr(ord(point)-1)
    print('\n')

