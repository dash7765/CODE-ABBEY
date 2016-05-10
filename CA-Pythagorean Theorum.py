#David Snider
#3/7/16

n = int(input())

out = []

for i in range(n):
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    numberToCheck = ((a**2)+(b**2))**0.5
    
    if c == numberToCheck:
        out.append('R')
    elif c > numberToCheck:
        out.append("O")
    else:
        out.append("A")
        
for i in out:
    print(i,end=' ')