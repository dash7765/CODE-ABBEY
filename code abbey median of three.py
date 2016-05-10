#David Snider
#2/18/16
import statistics

number = int(input())


out=[]
for i in range(0,number):
    numbers = str(input())
    num = numbers.split()
    for i in range(0, len(num)):
        num[i] = int(num[i])
    out.append(statistics.median(num))

for i in out:
    print(i,end=' ')
