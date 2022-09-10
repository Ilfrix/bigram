import pickle
import random as rand
import argparse

def generate_text(model_path, length, prefix) -> str:
    d = dict()
    
    with open(model_path, 'rb') as f:
        d = pickle.load(f)
    if (prefix == ()):
        r = rand.randint(0,1000)
        t = 0
        
        for bigram in d:    
            t += 1
            if (t == r):
                prefix = bigram
    print(prefix)
    #сделать префикс вариативным
    #prefix = ('мы', 'будем')
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
    
def main_generate(args):
    if (args == ()):
        parser = argparse.ArgumentParser(description='generation texts')
        parser.add_argument('model', type=str, help='Input model path\'s')
        parser.add_argument('--prefix', type=str, default='',help='Input dir for texts(default: stdin))')
        parser.add_argument('length', type=int, help='Input length of generate subsequence')
        args = parser.parse_args()
    prefix = tuple(args.prefix.split())
    length = args.length
    model = args.model
    s = generate_text(model, length, prefix)
    print(s)
    j = input('Enter something and press enter for closing')

if __name__ == '__main__':
    main_generate(())