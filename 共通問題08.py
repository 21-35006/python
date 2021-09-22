def mondai1():
    list=[1,2,3,4,5,6,7,8,9,10]
    for count in range(0,10):
        print('list[{}] = {}'.format(count,list[count]))
def mondai2():
    tpl1=('茨城県','栃木県','群馬県','千葉県','東京都','埼玉県','神奈川県',)
    for count in range(len(tpl1)):
        print(tpl1[count])
def mondai3():
    eve=[]
    odd=[]
    for count in range(10):
        num=int(input(str(count+1)+'件目：整数を入力 = '))
        if num%2==0:
            eve.append(num)
        else:
            odd.append(num)
    print('偶数配列 = [{}]'.format(eve))
    print('奇数配列 = [{}]'.format(odd))















def mondai13():
    tpl1=(int(input('学生番号=')),input('氏名='))
    tpl2=(int(input('学生番号=')),input('氏名='))
    tpl3=(int(input('学生番号=')),input('氏名='))
    print(tpl1,tpl2,tpl3,sep='\n')


def mondai14():
    dec={'野菜　　':'季節',
    'キャベツ':'春',
    "スイカ　":"夏",
    "ナス　　":"秋",
    "ハクサイ":"冬"}
    for kye,value in dec.items():
        print(kye,":",value,sep='')
def mondai15():
    dec={'野菜　　':'季節',
    'キャベツ':'春',
    "スイカ　":"夏",
    "ナス　　":"秋",
    "ハクサイ":"冬"}
    for kye,value in dec.items():
        print(kye,":",value,sep='')
        if value=='春'or value=='季節':
            break
def mondai16():
    dec={"id":100,
    'name':"大原太郎",
    'age':19,}
    dec.update(age=20)
    for kye,value in dec.items():
        print(kye,":",value,sep='')
def mondai17():
    dec={'国語':75,
    '算数':80,}
    dec2={'国語':75,
    '数学':80,}
    dec3={'国語': 75,
     '数学': 80, 
     '理科': 65,
     '社会': 90,
     '英語': 70}
    print(dec,dec2,dec3,sep="\n")
mondai17()