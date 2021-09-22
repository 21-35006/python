f=open('16_2_read.txt')
while True:
    line = f.readline()
    if not line:
        break
    print(line,end='')
f.close()