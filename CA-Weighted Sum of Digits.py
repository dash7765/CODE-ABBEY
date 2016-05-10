#David Snider
#3/3/16

data =  int(input())

out = []

numbers = input().split()

for number in numbers:
    total = 0
    for i in range(len(number)):
        total += int(number[i]) * (i+1)
    out.append(total)

for i in out:
    print(i,end=' ')
    
