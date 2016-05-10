#David Snider
#3/1/16

data = int(input())
punctuation = [',', '.', '-', ';', ':', '!', '?', ' ']
out = []


for i in range(data):
    words = input()
    word = ''
    reverse = ''
    for i in words:
        if i in punctuation:
            pass
        else:
            word += i

    word = word.lower()
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]

    if word == reverse:
        out.append('Y')
    else:
        out.append('N')

for i in out:
    print(i,end=' ')
