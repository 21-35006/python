def mondai1_2():
    print('a bc\nd e')

def mondai2_2():
    a=10.0
    b="10"
    c="十"
    int(a)
    int(b)
    #ウは変換不可

def mondai3_2():
    a=98
    b=76
    print(a,"-",b,"=",a-b)

def mondai4_2():
    print('0~100までの得点（整数値）を入力して下さい')
    JA=(int(input('国語の得点：')))
    EN=(int(input('英語の得点：')))
    if JA==100 and EN==100:
        print('満点です')

def mondai6_2():
    sum=0
    for count in range(100):
        sum+=count+1
    print('合計は{}です。'.format(sum))

def mondai14_2():
    x=input('文字列を入力：')
    print('入力された文字数は{}です。'.format(len(x)))
mondai14_2()
