moji="abc"+"def"
print(moji)
print('-'*10)
#インデックス
s='abcdef'
for i in range(len(s)):
    print('s[{}]={}'.format(i,s[i]))
#スライス式

print(s[0:3])
print(s[0:3:2])