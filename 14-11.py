moji=input('住所を入力して下さい：')
if moji.find('市')>=0:
    print('市')
elif moji.find('群')>=0:
    print('群')
else :
    print('東京23区')