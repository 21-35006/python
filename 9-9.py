from math import pi
def cm(r):
    cm=(r*2)*pi
    return round(cm,2)
def cm2(r):
    cm2=r**2*pi
    return round(cm2,2)
r=float(input('半径を入力して下さい：'))
cm=cm(r)
cm2=cm2(r)
print('半径',r,"の円の円周は",cm,sep='')
print('半径',r,'の面積は',cm2,sep='')