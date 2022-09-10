import random as rand
text = ''
with open("text2.txt", 'r', encoding='utf-8') as f:
    for line in f:
        text += line[:len(line)-1] + ' '
n = 2
new_text = ''
for i in range(len(text)):
    k = ord(text[i])
    #можно добавить точку в условие ниже
    if (k in range(65, 91) or k in range(97,122) or k in range(1040, 1104)):
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

for gram in d:
    value = 0
    for words in d[gram]:
        value += words[1]
    index = 0
    for words in d[gram]:
        d[gram][index] = [d[tuple(gram)][index][0] , int(d[tuple(gram)][index][1]) / value]
        index += 1

#запись модели в файл
value_words = 0
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write("NEW_VERSION\n")
    for gram in d:
        tmp = str(gram) + " : " + str(d[gram]) + '\n'
        f.write(tmp)
print('Enter two words')
first_word, second_word = map(str, input().split())
k = (first_word, second_word)
res = first_word + ' ' + second_word
value_words_end = 100
while value_words < value_words_end:
    index = 0
    r = rand.random()
    flag = False
    for i in d[k]:
        cur_v = d[k][index][1]
        if (r < cur_v):
            k = (k[1], d[k][index][0])
            res += ' ' + d[k][index][0]
            flag = True
            break
        else:
            cur_v += d[k][index][1]
    if (flag == False):
        k = (k[1], d[k][index][0])
        res += ' ' + d[k][index][0]
        index += 1
    value_words += 1
print(res)