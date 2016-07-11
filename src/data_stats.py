#For each dataset
# X
# Num tokens
# TTR
# Num sentences
# Y
# BIO
# H(Y)
# |Y|
# % of O

import argparse
from collections import Counter
from scipy.stats import entropy, kurtosis
import math
from sklearn.feature_extraction import DictVectorizer
import numpy as np
from sklearn import cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score



def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--train",   metavar="FILE", default="/Users/hector/proj/multisemantics/data/conll2003english_chunk/conll2003english_chunk_train.conll")
    parser.add_argument("--dev",   metavar="FILE", default="/Users/hector/proj/multisemantics/data/conll2003english_chunk/conll2003english_chunk_dev.conll")
    parser.add_argument("--test",   metavar="FILE", default="/Users/hector/proj/multisemantics/data/conll2003english_chunk/conll2003english_chunk_test.conll")

    args = parser.parse_args()

    wordcounter = Counter()
    labelcounter = Counter()
    previous = "O"
    n_sentences = 0
    bio = 0
    sentences = []
    word_accum= [(None,"^")]
    for line in open(args.train).readlines()+open(args.dev).readlines()+open(args.test).readlines():
        line = line.strip()
        if line:
            word,label = line.split("\t")
            wordcounter[word]+=1
            if label == "_":
                label = "O"
            labelcounter[label]+=1

            if label.startswith("B-"):
                bio = 1
            word_accum.append((word,label))
        else:
            word_accum.append((None,"$"))
            sentences.append(word_accum)
            word_accum = [(None,"^")]
            n_sentences+=1



    n_tokens = sum(wordcounter.values())
    ttr = len(wordcounter.keys()) /sum(wordcounter.values())
    proportion_of_O = labelcounter["O"] / float(sum(labelcounter.values()))
    number_of_labels = len(labelcounter.keys())
    entropy_of_labels = entropy(list(labelcounter.values()))
    kurtosis_of_labels = kurtosis(list(labelcounter.values()))
    entropy_of_nonempty_labels = entropy([labelcounter[k] for k in labelcounter.keys() if k != "O"])


    feats = []
    labels = []

    for s in sentences:
        for i in range(1,len(s)-1):
            prev_label = s[i-1][1]
            next_label = s[i+1][1]
            current_label = s[i][1]
            current_word = s[i][0]
            current_log_freq = int(math.log(wordcounter[current_word]))
            #print(prev_label,current_label,next_label,current_log_freq)
            feats.append({'prev:':prev_label, 'curr':current_label,'next':next_label})
            labels.append(current_log_freq)

    vec = DictVectorizer()
    X = vec.fit_transform(feats).toarray()
    Y = np.array(labels)

    linreg = LinearRegression()

    rsquares = []

    for TrainIndices, TestIndices in cross_validation.KFold(n=X.shape[0], n_folds=10, shuffle=False,
                                                            random_state=None):
        TrainX_i = X[TrainIndices]
        Trainy_i = Y[TrainIndices]

        TestX_i = X[TestIndices]
        Testy_i = Y[TestIndices]

        linreg.fit(TrainX_i, Trainy_i)
        ypred_i = linreg.predict(TestX_i)
        rsquares.append(r2_score(Testy_i,ypred_i))

    median_r_square = np.median(rsquares)
    print("\t".join([str(x) for x in [n_sentences,n_tokens,ttr,number_of_labels,bio,proportion_of_O,kurtosis_of_labels,entropy_of_labels,entropy_of_nonempty_labels,median_r_square]]))
if __name__ == "__main__":
    main()