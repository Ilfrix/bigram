import pickle
import os
import random as rand

class model_generate_text:

    def dir_read(self, path_dir) -> str:

        arr = os.listdir(path_dir)
        text = ''
        cur_f = 1
        #поиск .txt файлов и считывание данных из них
        for path in arr:
            path = path_dir + '/' + path
            print('обрабатывается ', path, ', прогресс', cur_f, '//', len(arr))
            cur_f += 1
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:    
                    text += line[:len(line)] + ' '
                    text = text.replace('\n', ' ' )
                text += '\n'
        return text


    def fit(self, args) -> None:
        path_dir = args.input_dir
        model = args.model
        
        if (path_dir != ''):
            text = self.dir_read(path_dir)
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
    
        
    
    def generate(self, args):
        d = dict()
        prefix = tuple(args.prefix.split())
        length = args.length
        model_path = args.model
        with open(model_path, 'rb') as f:
            d = pickle.load(f)
        if (prefix == ()):
            r = rand.randint(0,1000)
            t = 0
            
            for bigram in d:    
                t += 1
                if (t == r):
                    prefix = bigram
                    break
        value_words = 0
        res = prefix[0] + ' ' + prefix[1]
        
        while value_words < length:
            index = 0
            r = rand.random()
            flag = False
            for i in d[prefix]:
                
                cur_v = d[prefix][index][1]
                if (r < cur_v):
                    res += ' ' + d[prefix][index][0]
                    prefix = (prefix[1], d[prefix][index][0])
                    flag = True
                    break
                else:
                    cur_v += d[prefix][index][1]
                    index += 1
            
            if (flag == False):
                index -= 1
                res += ' ' + d[prefix][index][0]
                prefix = (prefix[1], d[prefix][index][0])
            value_words += 1
            
        return res