import math

class Circle:
    PI=3.1415
    def __init__(self,r:int):
        self.r = r 
        
    def circleline(self,r):
        line = self.r*2*Circle.PI
        return math.floor((line*10**3))/10**3

    def circlearea(self,r):
        area = (self.r**2*Circle.PI)
        return math.floor((area*10**3))/10**3
class Main:      
    def execute(self):
        en=Circle(int(input('半径を整数で入力：')))
        print('円周の長さは{}です。'.format(en.circleline(en.r)))
        print('円の面積は{}です。'.format(en.circlearea(en.r)))
main = Main()
main.execute()