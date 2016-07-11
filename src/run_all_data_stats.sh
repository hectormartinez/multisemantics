#!/usr/bin/env bash





for f in conll2003english_chunk conll2003english_ner framenet_framenames framenet_bioframeelements mpqa_coarse mpqa_polarity pos_ud_en semcor_semantictraits semcor_supersenses ud13english_deplabels
do
        train="/Users/hector/proj/multisemantics/data/"$f"/"$f"_train.conll"
        dev="/Users/hector/proj/multisemantics/data/"$f"/"$f"_dev.conll"
        test="/Users/hector/proj/multisemantics/data/"$f"/"$f"_test.conll"
        call=`python data_stats.py --train $train --test $test --dev $dev`
        outline=$f" "$call
    echo $outline
done