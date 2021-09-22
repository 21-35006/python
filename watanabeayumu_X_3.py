def mondai1_3():
    print('1|2|3,4,5')

def mondai2_3():
    a=str(100)
    b=str(100.0)
    c=str(-100)

def mondai3_3():
    a=23
    b=45
    print(a,'×',b,'=',a*b)

def mondai4_3():
    print('0~100までの得点（整数値）を２つ入力して下さい。')
    ten1=int(input('１つ目の得点：'))
    ten2=int(input('2つ目の得点：'))
    if ten1>=80 and ten2>=80:
        print('２科目とも合格です')

def mondai6_3():
    for count in range(10):
        print(count+1,end=' ')

def mondai14_3():
    moji=input('文字列を入力：')
    print('結果文字列：',end='')
    for i in range(10):
        print(moji[i],end='')
mondai14_3()