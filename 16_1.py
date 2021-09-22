f=open('16_1_read.txt')
while True:
    line = f.readline()
    if not line:
        break
    print(line,end='')
f.close()