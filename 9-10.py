def bmi(m,g):
    BMI=g/(m/100)**2
    return round(BMI,2)

def kg(m,g):
    Kg=(m/100)**2*22
    return round(Kg,2)

m=float(input('身長(cm)を入力して下さい：'))
g=float(input('体重(kg)を入力して下さい：'))
BMI=bmi(m,g)
Kg=kg(m,g)
print('BMI値は',BMI,'です')
print('適正体重は',Kg,'kgです')