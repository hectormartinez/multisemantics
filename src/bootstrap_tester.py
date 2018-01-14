import sys,re
import numpy as np
from scipy import stats
from sklearn import metrics
import random
from sklearn.metrics import accuracy_score,f1_score, classification_report
import argparse

def readlabels(infile,column):
    out = []
    for line in open(infile).readlines():
        line = line.strip()
        if line:
            out.append(line.split("\t")[column])
    return np.array(out)




def main():
    parser = argparse.ArgumentParser(description="")
    #parser.add_argument("--baseline", metavar="FILE",default="/Users/hmartine/Downloads/predictions/framenet_framenames/framenet_framenames_test.conll.baseline.task0")
    #parser.add_argument("--system", metavar="FILE",default="/Users/hmartine/Downloads/predictions/framenet_framenames/framenet_framenames_test.conll.framenet_framenames.aux.framenet_bioframeelements.task0")
    parser.add_argument("--baseline", metavar="FILE",default="/Users/hector/Dropbox/curro/predictions_ALL/pos_ud_en/pos_ud_en_test.conll.pos_ud_en.base.task0")
    parser.add_argument("--system", metavar="FILE",default="/Users/hector/Dropbox/curro/predictions_ALL/pos_ud_en/pos_ud_en_test.conll.pos_ud_en+pos.task0")
    parser.add_argument("--goldcolumn", type=int, default=1)
    parser.add_argument("--predictioncolumn", type=int, default=2)
    parser.add_argument("--iterations", type=int, default=1)

    args = parser.parse_args()
    gold = readlabels(args.baseline,args.goldcolumn)
    baseline = readlabels(args.baseline,args.predictioncolumn)
    system = readlabels(args.system,args.predictioncolumn)

    OUTLABELS = ["O","_"]
    violation_count = 0 #every time system is not over baseline
    print(classification_report(gold, system))
    print(classification_report(gold, baseline))


    #print(f1_score(gold, system))
    #print(f1_score(gold, baseline))

    accuracy_result = []
    f1_result = []
    for it in range(args.iterations):
        resample_i = np.random.randint(0, len(gold), len(gold))
        baseline_r = baseline[resample_i]
        system_r = system[resample_i]
        gold_r = gold[resample_i]

        f1_result.append(int(f1_score(gold_r, system_r) < f1_score(gold_r, baseline_r)))
        accuracy_result.append(int(accuracy_score(gold_r, system_r) < accuracy_score(gold_r, baseline_r)))

    #print(f1_result)
    #print(accuracy_result)
    print("F1-p",sum(f1_result)/len(f1_result))
    print("Acc-p", sum(accuracy_result) / len(accuracy_result))

if __name__ == "__main__":
    main()
