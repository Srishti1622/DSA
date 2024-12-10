# points to note for any paterns:
# - there will be nested looping mostly 2
# - outer loop is for new lines (rows) - count the number of lines or rows
# - inner loop for each new line (columns) - focus on the columns and connect them somehow to the rows
# - whatever we are printing, print them inside the inner loop 
# - observe symmetry (optional as not applicable for all patterns)

# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 1a: rectangle or square filled 
print('--------------------------------')
print('Rectangle or sqaure filled')
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print('\n')

# pattern 1b: hollow rectangle or square
print('--------------------------------')
print('hollow Rectangle or sqaure')
for i in range(1,n+1): 
    if i==1 or i==n:
        for j in range(n):
            print('*',end=' ')
    else:
        for j in range(n):
            if j==0 or j==n-1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
    print('\n')

# pattern 1c: Rectangle or sqaure filled number in order
print('--------------------------------')
print('Rectangle or sqaure filled number in order')
for i in range(2*n-1):
    for j in range(2*n-1):
        top=i
        bottom=j
        left=(2*n-2)-i
        right=(2*n-2)-j
        print(n-min(min(top,bottom),min(left,right)),end=' ')
    print('\n')