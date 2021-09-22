x=int(input('0~100までの国語の得点（整数値）を入力して下さい'))
if x>80:
    y=int(input('0~100までの英語の得点（整数値）を入力して下さい'))
    if y>=80:
        print('合格です')
    else :
        print('不合格です')
else:
     z=int(input('0~100までの数学の得点（整数値）を入力して下さい'))
     if z>=80:
         print('合格です')
     else:
         print('不合格です')