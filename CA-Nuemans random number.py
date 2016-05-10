#David Snider
#3/8/16

number = int(input())

out = []

entry = input().split()

for i in range(number):
    data = int(entry[i])
    numbers = [data]
    done = False
    x = data
    times = 0
    while done == False:
        times +=1
        x = x*x
        x = int(x/100)%10000
        if int(x) in numbers:
            done = True
        numbers.append(x)
    out.append(times)
    
for item in out:
    print(item,end=' ')