print('長方形を描画します。')
print('2~20までの整数値を入力して下さい。')
h=int(input('行数の入力：'))
if h>=2 and h<=20:
    l=int(input('列数の入力：'))
    if l>=2 and l<=20:
        for x in range(1,h+1):   
           print('*'*l)
    else:
        print('値が正しくありません。')
else:
   print('値が正しくありません。')