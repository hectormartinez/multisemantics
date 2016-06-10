__author__ = 'alonso'

from collections import Counter, defaultdict

from fnsentence import FrameArgument,FrameEntry,FrameSentence

import codecs
mwe_target_head_dict = {}

targetfolder = {}


targetfoldername="XXX"
for l in open("/Users/hmartine/proj/multisemantics/data/framenet_framenames/README.txt").readlines():
    l=l.strip()
    if l:
        if l.endswith(":"):
            targetfoldername=l[:-1]
        else:
            targetfolder[l] = targetfoldername
print(targetfolder)

for l in open("../res/pos_heads_for_mwe_targets.tsv").readlines():
    idx, key = l.strip().split("\t")
    idx = int(idx)
    mwe_target_head_dict[key] = idx

mwwtargets=0
targets=0
MWEs=Counter()
from nltk.corpus import framenet as fn
#from build_target_list import normalizeLemma
sentences = []

FrameElement_bitmasks = []
for d in fn.documents():
        for sentence in fn.annotated_document(d["ID"])["sentence"]:
            s = FrameSentence(sentence["text"])
            local_frame_elements = ["O"] * len(s.textlist)
            #print(len(s.offsetdict.keys()),(s.offsetdict),len(s.text.split(" ")))
            #print(sentence.keys())
            for annotation in sentence["annotationSet"]:
                 if "frameID" in annotation.keys():
                     signature = annotation["luName"]
                     lemma, pos = annotation["luName"].split(".")
                     #lemma = normalizeLemma(lemma)
                     frameID = str(annotation["frameID"])
                     framename = annotation["frameName"]
                     arguments = {}
                     for x in annotation["layer"]:
                         if x["name"] == "Target":
                             for l in x["label"]:
                                 targets+=1
                                 start = int(l["start"])
                                 end = int(l["end"])
                                 key = str(start)+":"+str(end)
                                 starttoken = s.char_to_word_mapping[start]
                                 endtoken = s.char_to_word_mapping[end]
                                 remark = ""
                                 if starttoken != endtoken:
                                     #dictkey = " ".join(s.textlist[starttoken:endtoken+1])+"\t"+" ".join(s.postags[starttoken:endtoken+1])
                                     dictkey = " ".join(s.postags[starttoken:endtoken+1])
                                     actualhead = starttoken+mwe_target_head_dict.get(dictkey,1)
                                     frameindex = actualhead
                                     remark = "MWE"
                                 else:
                                    frameindex = starttoken
                                 #print(framename,name,frameindex,s.textlist[frameindex],":",signature,s.text, remark)
                         elif x["name"] == "FE":
                             #print(x["label"])
                             for l in x["label"]:
                                 if "start" in l.keys(): #If the frame element is instantiated
                                    start = int(l["start"])
                                    end = int(l["end"])
                                    key = str(start)+":"+str(end)
                                    fe_name = l["name"]
                                    starttoken = s.char_to_word_mapping[start]
                                    endtoken = s.char_to_word_mapping[end]
                                    #print(fe_name,starttoken,endtoken)
                                    for t in range(starttoken,endtoken+1):
                                        if t == starttoken:
                                            local_frame_elements[t]="B-"+fe_name
                                        else:
                                            local_frame_elements[t] = "I-"+fe_name
                                    # TODO arguments.append(FrameArgument(fe_name,starttoken,endtoken))
                                    arguments[fe_name] = FrameArgument(fe_name,starttoken,endtoken)
                             #print(signature,framename,[str(a) for a in arguments])
                     s.addFrame(framename,frameindex,arguments)
                 else:
                    for layer in annotation["layer"]:
                        if layer["name"] == "PENN":
                            for l in layer["label"]:
                                start = int(l["start"])
                                end = int(l["end"])
                                postag = l["name"]
                                #key = str(start)+":"+str(end)
                                try:
                                    postoken = s.char_to_word_mapping[start]
                                    s.postags[postoken] = postag.upper()
                                except:
                                    print(start,postag,s.textlist,s.postags)
                            #print(" ".join([w+"/"+p for w,p in zip(s.textlist,s.postags)]))
            #s.pad_mismatched_spaces()
            sentences.append(s)
            FrameElement_bitmasks.append(local_frame_elements)


        outname = targetfolder[d["filename"]]+"/"+d["filename"].replace(".xml","")
        #fout = codecs.open(outname+".fn",mode="w",encoding="utf-8")
        #for s in sentences:
             #s.correct_indices()
        #     fout.write("\n".join(s.print_form_target())+"\n")
        #fout.close()


        outname = targetfolder[d["filename"]] + "/" + d["filename"].replace(".xml", "")
        # fout = codecs.open(outname+".fn",mode="w",encoding="utf-8")
        # for s in sentences:
        # s.correct_indices()
        #     fout.write("\n".join(s.print_form_target())+"\n")
        # fout.close()

        outname = targetfolder[d["filename"]] + "/" + d["filename"].replace(".xml", "")
        fout = codecs.open(outname+".fes",mode="w",encoding="utf-8")
        for s,f in zip(sentences,FrameElement_bitmasks):
            if f.count("O") == len(f):
                pass
            else:
                for w,t in zip(s.textlist,f):
                    fout.write(w+"\t"+t+"\n")
                fout.write("\t")
        sentences = []
        FrameElement_bitmasks = []