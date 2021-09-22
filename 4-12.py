n=int(input('西暦を入力して下さい'))
if n%4==0 and n%100!=0:
    print('閏年です')
elif n%400==0:
    print('閏年です')
else :
    print('平年です')