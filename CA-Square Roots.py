#Square Roots
#David Snider
#3/17/16

times = int(input())

out = []

for i in range(times):
    data = input().split()
    number = int(data[0])
    repeat = int(data[1])
    r = 1
    for x in range(repeat):
        r = (r+(number/r))/2
    out.append(r)
    
for item in out:
    print(item,end=' ')