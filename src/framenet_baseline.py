import argparse
from collections import Counter, defaultdict



def filterframe(x):
    if x == "_":
        return x
    else:
        return "TARGET"

def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--trainfile",   metavar="FILE", default="")
    parser.add_argument("--testfile",   metavar="FILE", default="")
    args = parser.parse_args()

    frame_dict = defaultdict(Counter)
    for line in open(args.trainfile):
        line = line.strip()
        if line:
            word,frame= line.split("\t")
            frame_dict[word][frame]=+1


if __name__ == "__main__":
    main()