#David Snider
#2/15/16


number = int(input())

def check(a,b):
    if '.5' in str(a/b):
        return True
    elif '.6' in str(a/b):
        return True
    elif '.7' in str(a/b):
        return True
    elif '.8' in str(a/b):
        return True
    elif '.9' in str(a/b):
        return True
    else:
        return False
out=[]
for i in range(0,number):
    numbers = str(input())
    num = numbers.split()
    a = int(num[0])
    b = int(num[1])
    if a/b < 0:
        if check(a,b):
            ab = int(a/b) - 1
        else:
            ab = int(a/b)
    else:
        if check(a,b):
            ab = int(a/b) + 1
        else:
            ab = int(a/b)
    out.append(ab)

for i in out:
    print(i,end=' ')
