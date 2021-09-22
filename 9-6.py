
def sum(list,sum):
    for i in range(len(list)):
        sum+=list[i]
    return sum
list=[4,10,59,679,1991,3994,6789,19324]
sum=sum(list,sum=0)
print('合計値 =',sum)