import argparse
from sklearn.metrics import classification_report



def filterframe(x):
    if x == "_":
        return x
    else:
        return "TARGET"

def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--infile",   metavar="FILE", default="../data/semcor_supersense/eng_semcor_test.conll")
    parser.add_argument("--labels",   metavar="FILE", default="framenet")
    args = parser.parse_args()
    if args.labels == "framenet":
        frames_pred = []
        frames_gold = []
        for line in open(args.infile):
            line = line.strip()
            if line:
                word,pred,gold = line.split("\t")
                frames_gold.append(gold)
                frames_pred.append(pred)
        targetdetection_gold = [ filterframe(x) for x in frames_gold]
        targetdetection_preds = [filterframe(x) for x in frames_pred]

        print(classification_report(targetdetection_gold,targetdetection_preds))
        print(classification_report(frames_gold,frames_pred))


if __name__ == "__main__":
    main()