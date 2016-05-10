#David Snider
#3/14/16
'''counts each number in an array'''


def check(numberToCheck,lookingFor):
    if int(numberToCheck) == int(lookingFor):
        return 1
    else:
        return 0


data = input().split()
m = int(data[0])
n = int(data[1])

data = input().split()

out = []

for i in range(n):
    total = 0
    for x in range(m):
        total += check(int(data[x]),int(i+1))
    out.append(total)
    
for item in out:
    print(item,end=' ')