def hantei(dic):
    sum=0
    for a,b in dic.items():
        if b>=60:
            print(a,'さんは合格です。',sep='')
        else:
            print(a,'さんは不合格です。',sep='')
        sum+=b
    print('平均点は、{}です。'.format(round((sum/3),2)))

dic={input('1人目の名前を入力して下さい：'):int(input('1人目の点数を入力して下さい：')),
input('2人目の名前を入力して下さい：'):int(input('2人目の点数を入力して下さい：')),
input('3人目の名前を入力して下さい：'):int(input('3人目の点数を入力して下さい：')),}
print('')

hantei(dic)