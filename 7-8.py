a=0
b=1
sum=0
while sum<=1000:
    print(a,end=',')
    sum =a+b
    a=b
    b=sum
print(a)