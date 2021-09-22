def san(n):
    return n*3
    

a=int(input('整数を入力してください：'))
s=san(a)
x=san(s)
print("{}の9倍は{}です。".format(a,x))