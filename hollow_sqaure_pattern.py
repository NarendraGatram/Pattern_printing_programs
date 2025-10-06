'''
    Pattern : Hollow Square Pattern
    Input : ex-> 5
    o/p:
        * * * * *
        *       *
        *       *
        *       *
        * * * * *
'''

n = int(input('Enter no of rows : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or j==n or i==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()