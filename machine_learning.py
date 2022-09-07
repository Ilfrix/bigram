text = ''
with open("text.txt") as f:
    for line in f:
        text += line[:len(line)-1] + ' '
        #text += line
#n = int(input())
n = 2
new_text = ''
for i in range(len(text)):
    k = ord(text[i])
    if (k in range(65, 91) or k in range(97,122) or k in range(1040, 1104) or text[i] == '.'):
        new_text += text[i]
    else:
        new_text += ' '
new_text = new_text.lower()
arr = []
arr = new_text.split()
d = dict()

for i in range(len(arr) - n):
    p = 0
    tmp = []
    while (p < n):
        tmp.append(arr[p+i])
        p += 1
    if (tuple(tmp) in d):
        word = arr[i + n]
        flag = False
        index = 0
        for w in d[tuple(tmp)]:
            if (word in w):
                d[tuple(tmp)][index] = [d[tuple(tmp)][index][0] ,d[tuple(tmp)][index][1] + 1]
                flag = True
                break
            index += 1
        if (flag == False):
            d[tuple(tmp)].append([arr[i + n], 1])
    else:
        d[tuple(tmp)] = [(arr[i + n], 1)]
#print(d)

for gram in d:
    value = 0
    #print(gram)
    for words in d[gram]:
        #print(words[1])
        value += words[1]
    index = 0
    for words in d[gram]:
        d[gram][index] = [d[tuple(gram)][index][0] , int(d[tuple(gram)][index][1]) / value]
        index += 1

print(d)