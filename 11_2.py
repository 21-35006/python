class Sum:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sigma(self,):
        total = 0

        for i in range(self.x,self.y+1):
            total+=i
        return total
    
class Main:

    def execute(self):
        sum =Sum(100,200)

        result = sum.sigma()
        print('{}から{}までの合計値は{}です。'.format(sum.x,sum.y,result))

main = Main()
main.execute()