import random
def ram():
    n=random.randint(1,4)
    return n
n=ram()
if n==1:
    print('本日の運勢：絶好調')
elif n==2:
    print('本日の運勢：好調')
elif n==3:
    print('本日の運勢：不調')
else :
    print('本日の運勢：絶不調')
