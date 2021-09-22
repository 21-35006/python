n=input('計算式を入力してください：')
s= []
print(n[0])
for i in range(0,len(n)):
    s.append(n[i])

if s in '+':
    print(x,'+',y,'=',x+y)