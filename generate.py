from class_model import generate


parser = argparse.ArgumentParser(description='generation texts')
parser.add_argument('--model', type=str, help='Input model path\'s')
parser.add_argument('--prefix', type=str, default='',help='Input dir for texts(default: stdin))')
parser.add_argument('--length', type=int, help='Input length of generate subsequence')
args = parser.parse_args()
generate(args)