f = open('16_4_write.txt','w')

while True:
    line=input('入力：')
    if line=='end':
        print('書き込み終了')
        break
    f.write('{}\n'.format(line))