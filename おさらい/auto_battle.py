import random
hp=random.random(50,200)
at=random.random(10,30)
sp=random.random(15,35)
mikata1={'名前':'勇者','HP':100,'攻撃力':20,'素早さ':20}
mikata2={'名前':'スライム','HP':50,'攻撃力':10,'素早さ':35}
mikata3={'名前':'ドラキー','HP':80,'攻撃力':15,'素早さ':30}
teki1={'名前':'敵','HP':hp,'攻撃力':at,'素早さ':sp}
jun=[mikata2,mikata3,mikata1]
if teki1['素早さ']>=20 and teki1['素早さ']<30:
    jun.insert(3,teki1)
elif teki1['素早さ']>=30 and teki1['素早さ']<=35:
    jun.insert(2,teki1)
else:
    jun.insert(4,teki1)
while True:
    if jun[1]!=teki1:
        teki1['HP']-jun[0,'攻撃力']
        print(jun[0],'の攻撃!\n',teki1,'に',jun[0,'攻撃力'],'のダメージ')
    else:
        n=random.random(1,3)
        if n==1:
            mikata1