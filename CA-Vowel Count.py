#David Snider
#2/16/16

number = int(input())
VOWELS = 'a e i o u y'.split()

def check(l,v=VOWELS):
    if l in v:
        return True
    else:
        return False
out = []

for i in range(0,number):
    word = input()
    total = 0
    for letter in word:
        if check(letter):
            total += 1
    out.append(total)

for i in out:
    print(i,end=' ')
