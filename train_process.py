import pickle
import os
import argparse

def dir_read(path_dir) -> str:

    arr = os.listdir(path_dir)
    text = ''
    #поиск .txt файлов и считывание данных из них
    for path in arr:
        path = path_dir + '/' + path
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:    
                text += line[:len(line)-1] + ' '
    return text


def create_model(path_dir, model) -> None:
    if (path_dir != ''):
        text = dir_read(path_dir)
    else:
        text = input('Dir\'s path not write, enter text:\n')

    n = 2   #биграмма
    new_text = ''
    #фильтрация неалфавитных символов русского и английского алфавитов
    for i in range(len(text)):
        k = ord(text[i])
        if (k in range(65, 91) or k in range(97,122) or k in range(1040, 1104)):
            new_text += text[i]
        else:
            new_text += ' '


    #приведение текста к нижнему регистру
    new_text = new_text.lower()
    arr = []
    arr = new_text.split()
    d = dict()


    #подсчет количества употреблений слов после биграм
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


    #перевод количества повторов в вероятность
    for gram in d:
        value = 0
        for words in d[gram]:
            value += words[1]
        index = 0
        for words in d[gram]:
            d[gram][index] = [d[tuple(gram)][index][0] , int(d[tuple(gram)][index][1]) / value]
            index += 1

    with open(model, 'wb') as f:
        pickle.dump(d, f)

def main_create(args):
    if (args == ()):
        parser = argparse.ArgumentParser(description='train model for generation texts')
        parser.add_argument('model', type=str, help='Input model path\'s')
        parser.add_argument('--input-dir', type=str, default='',help='Input dir for texts(default: stdin)')
        args = parser.parse_args()
    model = args.model
    input_dir = args.input_dir
    create_model(input_dir, model)
    j = input('Enter something and press enter for closing')

if __name__ == '__main__':  #удалить блок
    main_create(())