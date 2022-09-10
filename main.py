from train import main_create
from generate import main_generate
import argparse


#k = create_model(input_dir, model)
#d = generate_text(model, length, prefix)
#print(d)
class t:
    def fit():
        parser = argparse.ArgumentParser(description='train model for generation texts')
        parser.add_argument('--model', type=str, help='Input model path\'s')
        parser.add_argument('--input-dir', type=str, default='',help='Input dir for texts(default: stdin)')
        args = parser.parse_args()
        main_create(args)
    def generate():
        parser = argparse.ArgumentParser(description='generation texts')
        parser.add_argument('--model', type=str, help='Input model path\'s')
        parser.add_argument('--prefix', type=str, default='',help='Input dir for texts(default: stdin))')
        parser.add_argument('--length', type=int, help='Input length of generate subsequence')
        args = parser.parse_args()
        main_generate(args)

t.fit()