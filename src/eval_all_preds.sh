#!/usr/bin/env bash





for f in conll2003english_chunk conll2003english_ner framenet_framenames framenet_bioframeelements mpqa_coarse mpqa_polarity pos_ud_en semcor_semantictraits semcor_supersenses ud13english_deplabels
do
    outline=$f
    for system in .base.task0 +pos.task0 +pos_wsj.task0 +pos_udptb_en.task0 +pos.task1 +pos_wsj.task1 +pos_udptb_en.task1
    do
        predfile="/Users/hector/Downloads/predictions_ALL/"$f"/"$f"_test.conll."$f$system
        call=`python eval_preds.py --predictions $predfile --outlabel`
        outline=$outline" "$call
    done
    echo $outline
done