input_dir = './data/text2.txt'
model = './data/result2.txt'
flag = False #наличине готовой модели
start_version = "NEW_VERSION\n"
d = dict()

with open (model , 'r') as f:
    k = f.readline()
    if (k == start_version):
        flag = True

if (flag == True):
    with open (model, 'r', encoding = 'utf-8') as f:
        for line in f:
            if (line != start_version):
                tmp = line.split(':')
                key = tuple(tmp[0])
                new_key = ''
                #сиправить значение value
                new_value = ''
                value = tmp[1]
                #НУЖЕН РЕФАКТОРИНГ!!!!!!!!!!
                for i in range(len(key)):
                    if (key[i] == ' ' or key[i] == '\'' or key[i] == '(' or key[i] == ')'):
                        pass
                    else:
                        new_key += key[i]
                for i in range(len(value)):
                    if (value[i] == ' ' or value[i] == '\n' or value[i] == '\''):
                        pass
                    else:
                        new_value += value[i]
                #Делать это в цикле и у последнего элемента или единственного орезать на 1 разряд больше с конца
                new_value = new_value[1:len(new_value) - 1]
                #НУЖЕН РЕФАКТОРИНГ!!!!!!!!!!!!!!
                new_value = list(new_value.split('],'))
                arr = []
                for i in range(len(new_value)):
                    new_value[i] = new_value[i][1:len(new_value[i])]
                    if (i == len(new_value) - 1):
                        new_value[i] = new_value[i][:len(new_value[i]) - 1]
                    tmp = new_value[i].split(',')
                    tmp[1] = float(tmp[1])
                    arr.append(tmp)
                q = new_value[0]
                s = q.split(',')
                new_value = list(new_value)
                new_key = tuple(new_key.split(','))
                d[new_key] = (arr)
                
else:
    n = 2
    with open(input_dir, 'r', encoding='utf-8') as f:
        text = ''
        for line in f:
            text += line[:len(line)-1] + ' '
        new_text = ''
        for i in range(len(text)):
            k = ord(text[i])
            if (k in range(65, 91) or k in range(97,122) or k in range(1040, 1104)):
                new_text += text[i]
            else:
                new_text += ' '
    new_text = new_text.lower()
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