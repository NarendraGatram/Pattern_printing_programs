n = int(input('Enter no of rows : '))
for i in range(n):
    for j in range(n,0,-1):
        if j<=i:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
    