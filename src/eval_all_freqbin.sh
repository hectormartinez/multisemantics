#!/usr/bin/env bash





for f in conll2003english_chunk conll2003english_ner framenet_framenames mpqa_coarse pos_ud_en semcor_semantictraits semcor_supersenses ud13english_deplabels
do
    outline=$f
    for system in .base.task0 +pos.task0 +skewed10.task0 +skewed5.task0 +uniform5.task0 +pos_ud_en+skewed10.task0 +pos_ud_en+skewed5.task0 +pos_ud_en+uniform5.task0 +pos_udptb_en+skewed10.task0 +pos_udptb_en+skewed5.task0 +pos_udptb_en+uniform5.task0 +pos_udptb_en.task0 +pos_wsj+skewed10.task0 +pos_wsj+skewed5.task0 +pos_wsj+uniform5.task0 +pos_wsj.task0 +pos.task1 +pos_ud_en+skewed10.task1 +pos_ud_en+skewed5.task1 +pos_ud_en+uniform5.task1 +pos_udptb_en+skewed10.task1 +pos_udptb_en+skewed5.task1 +pos_udptb_en+uniform5.task1 +pos_udptb_en.task1 +pos_wsj+skewed10.task1 +pos_wsj+skewed5.task1 +pos_wsj+uniform5.task1 +pos_wsj.task1 +skewed10.task1 +skewed5.task1 +uniform5.task1 +pos_ud_en+skewed10.task2 +pos_ud_en+skewed5.task2 +pos_ud_en+uniform5.task2 +pos_udptb_en+skewed10.task2 +pos_udptb_en+skewed5.task2 +pos_udptb_en+uniform5.task2 +pos_wsj+skewed10.task2 +pos_wsj+skewed5.task2 +pos_wsj+uniform5.task2
    do
        predfile="/Users/hector/Downloads/predictions_freqbins/"$f"/"$f"_test.conll."$f$system
        call=`python eval_preds.py --predictions $predfile --outlabel`
        outline=$outline" "$call
    done
    echo $outline
done