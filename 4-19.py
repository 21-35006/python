print('0~100までの得点（整数値）を2つ入力して下さい')
n1=int(input('1つ目の得点:'))
n2=int(input('2つ目の得点:'))
if n1>=80 and n2>=80:
    print('合格です')
elif n1>=80 or n2>=80:
    print('補欠合格です')
else:
    print('不合格です')