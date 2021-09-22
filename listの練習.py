def mondai1():
     x=[3,15,123]
     print(x[1])
mondai1()

def mondai2():
    y=["3","ABCabc",12345,[10,20,"ABC"],333]
    print(y[3][1])


z=[]

z.append(225)
z.append(13)
z.append(50)
z.append(1002)
z.append(133)
z.append(99)
print(max(z),min(z))

z=sorted(z)
print(z)

z.reverse()
print(z)

print(z[2:5])

z[2:5]=[10,10,10]

a=[777,888,999]
z+=a
print(len(z))

z.insert(7,117)

del z[7]

z.clear()

del z
