
root='/Users/hmartine/Dropbox/curro/database.mpqa.3.0/man_anns'
for folder in `ls /Users/hmartine/Dropbox/curro/database.mpqa.3.0/gate_anns`
do
    for filename in `ls $root/$folder`
    do
        echo $filename

        docname=/Users/hmartine/Dropbox/curro/database.mpqa.3.0/docs/$folder/$filename
        annotationame=/Users/hmartine/Dropbox/curro/database.mpqa.3.0/man_anns/$folder/$filename/gateman.mpqa.lre.3.0
        python export_mpqa.py --doc $docname --annotations $annotationame --labels 'polarity' > sentiment/"$folder"_"$filename".polarity
    done

done



