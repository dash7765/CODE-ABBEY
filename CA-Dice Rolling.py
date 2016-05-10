#David Snider
#2/29/16

data = int(input())
out = []
for i in range(data):
    n = float(input())
    nOut = int(n*6)+1
    out.append(nOut)

for i in out:
    print(i,end=' ')
