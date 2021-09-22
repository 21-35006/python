def mondai4_1():
    ten=int(input("0~100 までの得点(整数値)を入力して下さい"))
    if ten>=80:
        print('合格です')

def mondai5_1():
    rank=(input('A~Dの値を入力して下さい：'))
    if rank=='A':
        print('ランクAは評価「優」です')
    elif rank=='B':
        print('ランクBは評価「良」です')
    elif rank=="C":
        print('ランクCは評価「可」です')
    else:
        print('ランクDは評価「不可」です')

def mondai6_1():
    for count in range(10):
        print("for文のプログラムです。")

def mondai7_1():
    n=1
    sum=0
    while n<=100:
        sum+=n
        n+=1
    print(sum)

def mondai14_1():
    print(input('文字列を入力：'))
mondai14_1()        