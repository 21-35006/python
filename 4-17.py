print('0~100までの得点（整数値）を入力して下さい')
a=int(input('1つ目の得点:'))
b=int(input('2つ目の得点:'))
if a<b:
    a, b = sorted([a,b],reverse=True)
    print(a,b)
elif a==b:
    print(a)
else:
    print(a,b)