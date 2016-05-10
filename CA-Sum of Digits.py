#David Snider
#2/22/16

dataNumber = int(input())

def do_math(a,b,c):
    return (a*b)+c
out = []
for i in range(dataNumber):
    numbers = input().split()
    total = 0
    for number in range(len(numbers)):
        numbers[number] = int(numbers[number])
    abc = do_math(numbers[0],numbers[1],numbers[2])
    for digit in str(abc):
        total += int(digit)
    out.append(total)

for i in out:
    print(i,end=' ')
    
