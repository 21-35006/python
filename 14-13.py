moji=input('住所を入力して下さい：')
to=moji.find('都')
dou=moji.find('道')
hu=moji.find('府')
ken=moji.find('県')
ku=moji.find('区')
si=moji.find('市')
gun=moji.find('郡')
if ken>=1:
    if si>=1:
        print('{}'.format(moji[ken+1:si+1:]))
    elif gun>=1:
        print('{}'.format(moji[ken+1:gun+1:]))
    else:
        print('{}'.format(moji[ken+1:ku+1:]))
elif dou>=1:
    if si>=1:
        print('{}'.format(moji[dou+1:si+1:])) 
    elif gun>=1:
        print('{}'.format(moji[dou+1:gun+1:]))
    else:
        print('{}'.format(moji[dou+1:ku+1:]))
elif hu>=1:
    if si>=1:
        print('{}'.format(moji[hu+1:si+1:]))
    elif gun>=1:
        print('{}'.format(moji[hu+1:gun+1:]))
    else:
        print('{}'.format(moji[hu+1:ku+1:]))
else :
    
    print('{}'.format(moji[to+1:ku+1]))
   