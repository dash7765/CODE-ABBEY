#Modular Calculator
#David Snider
#3/14/16

def do_math(sign,number,total):
    if sign == '+':
        return total + int(number)
    elif sign == '*':
        return total * int(number)
    elif sign == '%':
        return total % int(number)




total = int(input())

while True:
    dataIn = input().split()
    total = do_math(dataIn[0],dataIn[1],total)
    if dataIn[0] == '%':
        break

    
print(total) 