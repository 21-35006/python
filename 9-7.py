def iq(l,n):
    for i in range(len(list)):
        if n==list[i]:
            return 1
list=[4,10,59,679,1991,3994,6789,19324]
n=int(input('整数を入力してください：'))
re=iq(list,n)
if re==1:
    print(n,'は配列に含まれています。')
else:
    print(n,'は配列に含まれていません。')