#David Snider
#2/19/16


number = int(input())

bmi = 0
out=[]

def check(BMI):
    if BMI < 18.5:
        return 'under'
    elif BMI >= 18.5 and BMI < 25.0:
        return 'normal'
    elif BMI >= 25.0 and BMI < 30.0:
        return 'over'
    else:
        return 'obese'

def calculate(height, weight):
    out = float(weight/(height**2))
    return out

for i in range(0,number):
    numbers = input()
    num = numbers.split()
    w = int(num[0])
    h = float(num[1])
    bmi = calculate(h,w)
    out.append(check(bmi))

for i in out:
    print(i,end=' ')
