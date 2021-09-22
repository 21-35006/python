n=int(input("整数値"))

if n>0:
    print('その値は正です。')
else:
    print("その値は負です。")

if n>0:
    print("その値は正です。")
elif n==0:
    print('その値は0です。')
else :
    print('その値は負です。')
print('プログラムを終了します。')

#List3-20
a=int(input('整数a'))
b=int(input('整数b'))

min2=a if a < b else b 

print('小さいほうの値は',min2,'です。')

if n>0:
    if n%2==0:
        print('その値は正の偶数です。')
    else:
        print('その値は正の奇数です。')
else:
    print('その値は正ではないです。')

a=int(input('整数a'))
b=int(input('整数b'))

a,b= sorted([a,b])
#ソート(交換)の関数

print('昇順に並べると',a,b)