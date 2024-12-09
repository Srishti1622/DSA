# points to note for any paterns:
# - there will be nested looping mostly 2
# - outer loop is for new lines (rows) - count the number of lines or rows
# - inner loop for each new line (columns) - focus on the columns and connect them somehow to the rows
# - whatever we are printing, print them inside the inner loop 
# - observe symmetry (optional as not applicable for all patterns)

# getting the n value from user
n=int(input("Enter the value of N: "))

# pattern 1: rectangle or square filled 
print('--------------------------------')
print('Rectangle or sqaure filled')
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print('\n')