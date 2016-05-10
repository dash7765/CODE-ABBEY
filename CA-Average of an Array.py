#David Snider
#2/23/16


number = int(input())

out=[]
for i in range(0,number):
    numbers = input().rstrip('0').split()
    total = 0
    for i in numbers:
        total += int(i)
    average = total/len(numbers)
    if '.5' in str(average):
        average += .5
    out.append(round(average))

for i in out:
    print(i,end=' ')
