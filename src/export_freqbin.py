
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

def uniformbin(rankedwords,word,k=5):
    binlength = int(len(rankedwords) / k)
    if word in rankedwords:
        return int(rankedwords.index(word) / binlength)
    else:
        return 0




def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--training",   metavar="FILE", default="/Users/hector/Downloads/predictions_WSJ/conll2003english_ner/conll2003english_ner_test.conll.conll2003english_ner+pos.task0")
    parser.add_argument("--infile",   metavar="FILE", default="/Users/hector/Downloads/predictions_WSJ/conll2003english_ner/conll2003english_ner_test.conll.conll2003english_ner+pos.task0")
    parser.add_argument("--binning", default="uniform")
    parser.add_argument("--k", default=10)

    args = parser.parse_args()

    C = Counter(words(args.training))

    if args.binning == "skewed":
        bins = {word: skewedbin(C[word],base=args.k) for word in words(args.training) }
    else:
        Cacc = Counter()
        acc = 0
        for word,freq in reversed(C.most_common()):
            Cacc[word]=acc+freq
            acc=Cacc[word]

        freqs = list(Cacc.values())
        bins = numpy.linspace(0,max(freqs),num=args.k)
        hist,bin_edges = numpy.histogram(freqs, bins, weights=freqs)
        cumsumbins = numpy.cumsum(hist)
        digitized = numpy.digitize(freqs, cumsumbins)
        print(list(reversed(Cacc.most_common())))


        rankedwords=list(reversed([x for x, y in C.most_common()])) # Reverse so that label 0 means the same for both skewed and uniform
        bins = {word: uniformbin(rankedwords,word,k=args.k) for word in words(args.training) }


    for line in open(args.infile).readlines():
        line = line.strip()
        if line:
            w = line.split("\t")[0]
            #print(w+"\t"+str(bins.get(w,0)))
        else:
            pass
            #print


if __name__ == "__main__":
    main()