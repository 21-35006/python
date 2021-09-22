moji=input('住所を入力して下さい：')
to=moji.find('都')
dou=moji.find('道')
hu=moji.find('府')
ken=moji.find('県')
if ken>=1:
   print('{}'.format(moji[ken+1:]))
elif dou>=1:
   print('{}'.format(moji[dou+1:]))
elif hu>=1:
   print('{}'.format(moji[hu+1:]))
else :
   print('{}'.format(moji[to+1:]))
   