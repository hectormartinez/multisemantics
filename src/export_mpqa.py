import argparse
from collections import Counter, defaultdict
import re
import sys
from nltk.tokenize import wordpunct_tokenize

def get_polarity_label(line):
        m = re.search('polarity="(.+?)"',line)
        if m:
            if m.group(1):
                return m.group(1)
            else:
                print("NA2"+line, file=sys.stderr)
        else:
            print("NA1" + line, file=sys.stderr)
            #return "negative" #this is a patch for a disagreement that yields a spurious match in the data, NOT a backoff
def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--doc",   metavar="FILE", default="/Users/hmartine/Downloads/database.mpqa.3.0/docs/20011024/21.53.09-11428")
    parser.add_argument("--annotations",   metavar="FILE", default="/Users/hmartine/Downloads/database.mpqa.3.0/man_anns/20011024/21.53.09-11428/gateman.mpqa.lre.3.0")
    parser.add_argument("--labels", choices=['coarse','polarity'],default='coarse')
    args = parser.parse_args()

    docstring = open(args.doc).read()

    spanlabels = {}
    subjectives = {}
    sentences = {}

    if args.labels == 'coarse':
        for line in open(args.annotations).readlines():
            if line.startswith('#'):
                pass
            else:
                begin,end = line.strip().split("\t")[1].split(',')
                begin = int(begin)
                end = int(end)
                label = line.strip().split("\t")[2]
                if label in ['direct-subjective','attitude','expressive-subjectivity','objective-speech-event'] and end > begin: #we skip implicit
                    subjectives[begin] = end
                    spanlabels[begin] = label
                elif "sentence" in line:
                    sentences[begin] = end
    else:
        for line in open(args.annotations).readlines():
            if line.startswith('#'):
                pass
            else:
                begin, end = line.strip().split("\t")[1].split(',')
                begin = int(begin)
                end = int(end)
                if re.search('polarity="(.+?)"',line) and end > begin:  # we skip implicit
                    subjectives[begin] = end
                    label = get_polarity_label(line)
                    spanlabels[begin] = label
                elif "sentence" in line:
                    sentences[begin] = end
    #print(sorted(spanlabels.keys()))
    #print(sorted(subjectives.keys()))
    #print(sorted(sentences.keys()))
    del(begin)
    del(end)
    del(label)

    for sentence_start in sorted(sentences.keys()):
        visited = []
        sentence_end = sentences[sentence_start]
        acc = ""

        for i in range(sentence_start, sentence_end):
            if i in visited:
                pass
            elif i in subjectives.keys():
                for t in wordpunct_tokenize(acc.strip()):
                    if t:
                        print(t + "\tO")
                acc = ''
                spanout = docstring[i:subjectives[i]]
                for j,t in enumerate(wordpunct_tokenize(spanout.strip())):
                    currentlabel = spanlabels[i]
                    if j == 0:
                            outlabel = "B-"+currentlabel
                    else:
                            outlabel = "I-"+currentlabel
                    print(t+"\t"+outlabel)
                visited.extend(range(i,subjectives[i]))
            else:
                acc+=docstring[i]
        for t in wordpunct_tokenize(acc.strip()):
            if t:
                print(t+"\tO")
        print()



if __name__ == "__main__":
    main()