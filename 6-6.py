start=int(input('開始数：'))
end=int(input('終了数：'))
sum=0
for count in range(start,end+1):
    sum+=count
print('合　計：',sum,sep='')
