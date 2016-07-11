
for epochs in .i5. .i15. .i30. .i50.
do
for task in conll2003english_ner framenet_framenames mpqa_coarse semcor_semantictraits semcor_supersenses
do
    taskfile=$task"_test.conll"
for f in `ls /Users/hector/tmp/predictions-5m-4aux/*/*$taskfile*$epochs*task0`
do
    call=`python eval_preds.py --predictions $f --outlabel`
    echo "$epochs $f $call"
done
done
done