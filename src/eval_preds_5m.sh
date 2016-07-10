#!/usr/bin/env bash
for iterations in .i5 .i15 .i30 .i50
do
    for layer in .o3.1 .o3.3 .o3.1.1 .o3.1.1.1 .o3.3 .o3.3.3 .o3.3.3.3
    do
        for f in conll2003english_ner framenet_framenames mpqa_coarse semcor_semantictraits semcor_supersenses
        do
            outline="$iterations $layer $f"
            for aux in conll2003english_chunk conll2003english_chunk+uniform5 pos_ud_en pos_ud_en+conll2003english_chunk pos_ud_en+ud13english_deplabels pos_ud_en+uniform5 ud13english_deplabels ud13english_deplabels+conll2003english_chunk ud13english_deplabels+uniform5 uniform5
            do
                for task in .task0
                do
                    ss="$aux$iterations$layer$task"
                    predfile="/Users/hector/tmp/predictions-5m-4aux/"$f"/"$f"_test.conll.$f"+"$ss"
                    #wc -l "$predfile"
                    call=`python eval_preds.py --predictions $predfile --outlabel`
                    outline=$outline" - "$call
                 done
        done
     echo $outline

    done
done
done