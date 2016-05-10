#David Snider
#2/16/16


numbers = input().split()
number = int(numbers[0])
out=[]
c = 0
for i in range(1,number+1):
    f = int(numbers[i])
    c = (f - 32)/1.8000
    out.append(round(c))

for i in out:
    print(i,end=' ')
