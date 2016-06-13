import argparse
from collections import Counter, defaultdict



def normalizebio(label,previous):
    if label.startswith("I-") and previous == "O":
        label = "B"+label[1:]
    elif label.startswith("I-") and previous.startswith("B-"):
        pass
    elif label.startswith("I-") and previous.startswith("I-") and label != previous : #consecutive spans of different type
        label = "B" + label[1:]
    return label


def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--infile",   metavar="FILE", default="")
    args = parser.parse_args()

    previous = "O"
    for line in open(args.infile):
        line = line.strip()
        if line:
            word,label = line.split(" ")
            labelnew = normalizebio(label,previous)
            previous = label
            print(word+"\t"+labelnew)
        else:
            previous = "O"


if __name__ == "__main__":
    main()