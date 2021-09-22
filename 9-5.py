def math(x,y):
    print(x,"+",y,"=",x+y,sep="")
    print(x,"-",y,"=",x-y,sep="")
    print(x,"*",y,"=",x*y,sep="")
    print(x,"/",y,"=",int(x/y),sep="")
    print(x,"%",y,"=",x%y,sep="")
x=int(input('整数を入力してください：'))
y=int(input('整数を入力してください：'))
math(x,y)