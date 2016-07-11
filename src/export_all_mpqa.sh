
root='/Users/hector/Dropbox/curro/database.mpqa.3.0/man_anns'
for folder in `ls /Users/hector/Dropbox/curro/database.mpqa.3.0/gate_anns`
do
    for filename in `ls $root/$folder`
    do
        echo $filename

        docname=/Users/hector/Dropbox/curro/database.mpqa.3.0/docs/$folder/$filename
        annotationame=/Users/hector/Dropbox/curro/database.mpqa.3.0/man_anns/$folder/$filename/gateman.mpqa.lre.3.0
        python export_mpqa.py --doc $docname --annotations $annotationame --labels 'coarse' > sentiment/"$folder"_"$filename".coarse
    done

done



