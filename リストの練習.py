# print('合計点と平均点を求めます。') 
# n=int(input('学生の人数：')) 
# x=[] 
# sum=0 
# for count in range(n): 
#     x.append(int(input('{}番目の点数：'.format(count+1)))) 
#     sum+=x[count]
# print('合計点は{}点です。'.format(sum))
# print('平均点は{}点です。'.format(sum/n))

def mondai15():
    print("合計点と平均点を求めます。")
    print('：注"End"で入力終了')
    ten=[]
    a=1
    x=0
    total=0
    while True:
        x=(input('{}番目の点数：'.format(a)))
        if x=="End":
            break
        else:
            ten.append(int(x))
        total+=ten[a-1]
        a+=1
    print("合計は{}点です。".format(total))
    print("平均は{}点です。".format(total/(a-1)))
mondai15()