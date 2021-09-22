import datetime
now=datetime.datetime.now()

# ユーザーの名前を入力
user=input('名前を入力して下さい')

# 時間によって挨拶を変えるための分岐
if now.hour >= 10 and now.hour<=18:
     print('こんにちは',user,'さん')
elif now.hour>=18 or now.hour<=4:
    print('こんばんは',user,'さん')
else:
    print('おはようございます',user,'さん')

def wareki():
    year = int(input('西暦を入力して下さい'))
    while year<1868:
        print('その年には対応していません')
        year = int(input('もう一度西暦を入力して下さい'))
    if year >1868 and year<1912:
        print('その年は明治{}年です。'.format(year-1867))
    elif year==1868:
        print('その年は明治元年です。')
    elif year >1912 and year<1926:
        print('その年は大正{}年です。'.format(year-1911))
    elif year ==1912:
        print('その年は大正元年です。')
    elif year >1926 and year<1989:
        print('その年は昭和{}年です。'.format(year-1925))
    elif year ==1926:
        print('その年は昭和元年です。')
    elif year >1989 and year<2019:
        print('その年は平成{}年です。'.format(year-1988))
    elif year ==1989:
        print('その年は平成元年です。')
    elif year >2019 :
        print('その年は令和{}年です。'.format(year-2018))
    elif year ==2019:
        print('その年は令和元年です。')

def keisan():
    n=int(input('１つ目の整数を入力してください：'))
    m=input('計算記号を入力してください')
    l=int(input('２つ目の整数を入力してください：'))
    if m == '+':
        print('答え：{}'.format(n+l))
    elif m == '-':
        print('答え：{}'.format(n-l))
    elif m == '×':
        print('答え：{}'.format(n*l))
    elif m == '÷':
        print('答え：{}'.format(n/l))
    elif m == '%':
        print('答え：{}'.format(n%l))

keisan()