n=int(input('整数値を入力して下さい'))
for line in range(1,n):
    for count in range(1,line):
        x=round( int((n-line)))
        if count==1:
         for sp in range(1,x):
            print(' ',end='')
    
        print('{}'.format("＊"),end='')
    print()