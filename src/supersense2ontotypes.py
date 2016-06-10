import argparse
import sys
from collections import Counter, defaultdict


parser = argparse.ArgumentParser(description="")
parser.add_argument("--infile",   metavar="FILE", default="../data/semcor_supersense/eng_semcor_test.conll")
parser.add_argument("--ontotypes",   metavar="FILE", default="../res/map_ontotypes_to_supersense_freqsorted.tsv")
parser.add_argument("--bio",   default=False, action='store_true')

args = parser.parse_args()


semtypes = {}
supersenselist = set()

#for line in open(args.ontotypes).readlines():
#    sem, freq, supersenses = line.strip().split("\t")
#    for s in supersenses.split(";"):
#        supersenselist.add(s)

for line in open(args.ontotypes).readlines():
    sem, freq, supersenses = line.strip().split("\t")
    for s in supersenses.split(";"):
        s = s.strip()
        if s not in semtypes:
            semtypes[s]=sem

#for s in sorted(semtypes.keys()):
#    print(len(semtypes[s]),s,semtypes[s])


def replace_label(label,lookup,bio):
    if len(label) < 2:
        return label
    else:
        if label.startswith("B-") or label.startswith("I-"):
            prefix = label[0:2]
            outlabel= lookup[label[2:]]
        else:
            outlabel = lookup[label]
        if bio:
            outlabel = prefix+outlabel
        return outlabel

for line in open(args.infile).readlines():
    line = line.strip()
    if line:
        word,label = line.split("\t")
        print(word+"\t"+replace_label(label,semtypes,args.bio))
    else:
        print()