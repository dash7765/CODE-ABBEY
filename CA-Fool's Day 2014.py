#David Snider
#3/10/16

times = int(input())

out = []

for i in range(times):
    data = input().split()
    total = 0
    for n in data:
        total += int(n)**2
    out.append(total)
    
for i in out:
    print(i,end=' ')