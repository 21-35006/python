x=int(input('国語の得点を入力して下さい'))
y=int(input('数学の得点を入力して下さい'))
z=int(input('英語の得点を入力して下さい'))
if x+y+z>=230:
    print('合格です')
elif x+y+z>=210 and (x>=85 or y>=85 or z>=85):
    print('合格です')
else :
    print('補講対象です')