import argparse

from class_model import model_generate_text
    
def main_generate(args):
    if (args == ()):
        parser = argparse.ArgumentParser(description='generation texts')
        parser.add_argument('--model', type=str, default='', help='Input model path\'s')
        parser.add_argument('--prefix', type=str, default='',help='Input dir for texts(default: stdin))')
        parser.add_argument('--length', type=int, default='', help='Input length of generate subsequence')
        args = parser.parse_args()
    s = model_generate_text()
    s = s.generate(args)
    print(s)
    j = input('Enter something and press enter for closing')

if __name__ == '__main__':
    main_generate(())