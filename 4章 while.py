  #List 4-1
from typing import Counter


a=int(input('整数a:'))
b=int(input('整数b:'))

a,b=sorted([a,b])

counter=a
while counter<=b:
    print(counter,end='')
    counter=counter+1
print()

#list 4-4

print('1からnまでの和を求めます。')

while True:
    n=int(input('nの値:'))
    if n>0:
        break

sum = 0
i=1
while i<=n:
    sum +=i
    i+=1
print('1から',n,'までの和は',sum,'です。')