#David Snider
#3/2/16

data = int(input())

out = []

PLACES = {}
numbers = input().split()
numberList = []
for i in range(1, data+1):
    PLACES[int(numbers[i-1])] = i

for i in range(len(numbers)):
    numberList.append(int(numbers[i]))

numberList.sort()

for i in numberList:
    out.append(PLACES[i])

for i in out:
    print(i,end=' ')
