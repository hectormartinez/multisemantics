
import argparse,math,numpy

from collections import Counter

def words(infile):
    w = []
    for line in open(infile).readlines():
        line = line.strip()
        if line:
            word = line.split("\t")[0]
            w.append(word)
    return w



def skewedbin(freq,base=10):
    return int(math.log(freq,base))


def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--trainfile",   metavar="FILE", default="../data/conll2003english_chunk/conll2003english_chunk_test.conll")
    parser.add_argument("--infile",   metavar="FILE", default="../data/conll2003english_chunk/conll2003english_chunk_test.conll")
    parser.add_argument("--binning", default="skewed")
    parser.add_argument("--k", default=10,type=int) #this parameter is ambiguous, it is either the base of the log for skewed or the number of bins

    args = parser.parse_args()

    C = Counter(words(args.trainfile))

    if args.binning == "skewed":
        bins = {word: skewedbin(C[word],base=args.k) for word in words(args.trainfile) }
    else: #corresponds with uniform
        acc = 0
        total = sum( C.values())
        thresholds=numpy.linspace(0, total, num=args.k+1)
        offset=0
        bins = {}
        for word,freq in reversed(C.most_common()):
            acc=acc+freq
            if acc > thresholds[offset+1]:
                offset+=1
            bins[word]=offset

    for line in open(args.infile).readlines():
        line = line.strip()
        if line:
            w = line.split("\t")[0]
            print(w+"\t"+str(bins.get(w,0)))
        else:
            print()


if __name__ == "__main__":
    main()