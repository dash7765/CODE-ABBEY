#David Snider
#3/8/16

data = input().split()
already = []

out = []
for w in data:
    if w in already:
        if w in out:
            pass
        else:
            out.append(w)
    else:
        already.append(w)
        
out.sort()

for item in out:
    print(item,end=' ')