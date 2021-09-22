n=int(input('入力値：'))
for count in range(2,n):
    if n%count==0:
        print(n,'は素数ではありません。')
        break
else:
        print(n,'は素数です。')