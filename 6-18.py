print('カレンダーを表示させます。')
print('0：日　1：月　2：火　3：水　4：木　5：金　6：土')
day=int(input('表示させたい月は何曜日から始まりますか：'))
date=int(input('表示させたい月は何日ありますか：'))
print('日 月 火 水 木 金 土')
for counter in range(0,day):
    print('　',end=' ')
for count in range(1,date+1):
    if count<=9:
        print('',count,'',end='')
        day+=1
        if day==7:
            print()
            day=0
        continue
    print(count,end=' ')  
    #print('{:2d}'.format(count),end=' ')

    day+=1
    if day==7:
        print()
        day=0
    