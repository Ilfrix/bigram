import argparse
from class_model import model_generate_text

def main_create(args):

    if (args == ()):
        parser = argparse.ArgumentParser(description='train model for generation texts')
        parser.add_argument('--model', type=str, default='', help='Input model path\'s')
        parser.add_argument('--input-dir', type=str, default='',help='Input dir for texts(default: stdin)')
        args = parser.parse_args()
    
    f = model_generate_text()    
    f.fit(args)
    j = input('Enter something and press enter for closing')

if __name__ == '__main__':  #удалить блок
    
    main_create(())