from class_model import fit

parser = argparse.ArgumentParser(description='train model for generation texts')
parser.add_argument('--model', type=str, help='Input model path\'s')
parser.add_argument('--input-dir', type=str, default='',help='Input dir for texts(default: stdin)')
args = parser.parse_args()
fit(args)