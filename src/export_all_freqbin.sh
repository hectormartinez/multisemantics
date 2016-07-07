#!/usr/bin/env bash
base="/Users/hector/proj/multisemantics/data"
for task in conll2003english_chunk conll2003english_ner framenet_framenames mpqa_coarse pos_ud_en semcor_semantictraits semcor_supersenses ud13english_deplabels
do
suffix="skewed10"
outfolder=$base"/"$task"_"$suffix
mkdir $outfolder
python export_freqbin.py --binning skewed --k 10 --trainfile $base"/"$task"/"$task"_train.conll" --infile $base"/"$task"/"$task"_train.conll" > $outfolder"/"$task"_"$suffix"_train.conll"
python export_freqbin.py --binning skewed --k 10 --trainfile $base"/"$task"/"$task"_train.conll" --infile $base"/"$task"/"$task"_test.conll" > $outfolder"/"$task"_"$suffix"_test.conll"
python export_freqbin.py --binning skewed --k 10 --trainfile $base"/"$task"/"$task"_train.conll" --infile $base"/"$task"/"$task"_dev.conll" > $outfolder"/"$task"_"$suffix"_dev.conll"

suffix="skewed5"
outfolder=$base"/"$task"_"$suffix
mkdir $outfolder
python export_freqbin.py --binning skewed --k 5 --trainfile $base"/"$task"/"$task"_train.conll" --infile $base"/"$task"/"$task"_train.conll" > $outfolder"/"$task"_"$suffix"_train.conll"
python export_freqbin.py --binning skewed --k 5 --trainfile $base"/"$task"/"$task"_train.conll" --infile $base"/"$task"/"$task"_test.conll" > $outfolder"/"$task"_"$suffix"_test.conll"
python export_freqbin.py --binning skewed --k 5 --trainfile $base"/"$task"/"$task"_train.conll" --infile $base"/"$task"/"$task"_dev.conll" > $outfolder"/"$task"_"$suffix"_dev.conll"

suffix="uniform5"
outfolder=$base"/"$task"_"$suffix
mkdir $outfolder
python export_freqbin.py --binning uniform --k 5 --trainfile $base"/"$task"/"$task"_train.conll" --infile $base"/"$task"/"$task"_train.conll" > $outfolder"/"$task"_"$suffix"_train.conll"
python export_freqbin.py --binning uniform --k 5 --trainfile $base"/"$task"/"$task"_train.conll" --infile $base"/"$task"/"$task"_test.conll" > $outfolder"/"$task"_"$suffix"_test.conll"
python export_freqbin.py --binning uniform --k 5 --trainfile $base"/"$task"/"$task"_train.conll" --infile $base"/"$task"/"$task"_dev.conll" > $outfolder"/"$task"_"$suffix"_dev.conll"


done