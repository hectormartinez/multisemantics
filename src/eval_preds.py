import argparse
from sklearn.metrics import classification_report,accuracy_score,f1_score

"Angry   ADJ     PROPN"

outlabels = ["_","O"]



def flatread(infile):
    golds = []
    preds = []
    for line in open(infile).readlines():
        line = line.strip()
        if line:
            word, gold, pred = line.split("\t")
            golds.append(gold)
            preds.append(pred)
    return (golds,preds)

def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--predictions",   metavar="FILE", default="/Users/hector/Downloads/predictions_WSJ/conll2003english_ner/conll2003english_ner_test.conll.conll2003english_ner+pos.task0")
    parser.add_argument("--labels",   metavar="FILE", default="plain")
    parser.add_argument("--outlabel", action="store_true")
    args = parser.parse_args()

    if args.labels == "framenet":
        pass

    golds,preds = flatread(args.predictions)
    if args.outlabel:
        golds_filtered = []
        preds_filtered = []
        for g,p in zip(golds,preds):
            if g in outlabels:
                pass
            else:
                golds_filtered.append(g)
                preds_filtered.append(p)
    else:
        golds_filtered = golds
        preds_filtered = preds
    #print(classification_report(golds_filtered,preds_filtered))
    #print(accuracy_score(golds_filtered,preds_filtered))
    print(f1_score(golds_filtered,preds_filtered,average='micro'))


if __name__ == "__main__":
    main()