#Rotate String
#David Snider
#3/15/16


def rotate_string(txt):
    number = int(txt[0])
    string = txt[1]
    out = ''
    if str(number)[0] == '-':
        for i in range(number,len(string)+number):
            out += string[i]
        for i in range(0,number):
            out += string[i]
    else:
        for i in range(number,len(string)):
            out += string[i]
        for i in range(0,number):
            out += string[i]        
    return out


times = int(input())

outList = []

for i in range(times):
    data = input().split()
    outList.append(rotate_string(data))
    
for item in outList:
    print(item,end=' ')