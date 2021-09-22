import random


class Sum:
    def sigma(self,x,y):
        total=0
        for i in range(x,y):
            total+=i
        return total

class Main:
    def excute(self):
        x=100
        y=200
        sum=Sum()

        result=sum.sigma(x,y)
        print('{}から{}までの合計値は{}です。'.format(x,y,result))

main = Main()
main.excute()

