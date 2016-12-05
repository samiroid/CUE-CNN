import cPickle
import csv
from my_utils import preprocess
from my_utils import embeddings as emb_utils
from my_utils import word_2_idx
from my_utils import kfolds
import codecs
import pprint
from pdb import set_trace
import os

EMB_PATH_IN  = "DATA/embeddings/words.txt"
EMB_PATH_OUT = "DATA/embeddings/filtered_embs.txt"
TXT_IN       = "DATA/txt/bamman_redux.txt"
TXT_OUT      = "DATA/txt/bamman_clean.txt"
FOLDS =  "DATA/folds/"
idz = []

def build_folds(msg_ids):
    if not os.path.isdir(FOLDS):
        os.mkdir(FOLDS)
    kf = kfolds(10, len(msg_ids),val_set=True,shuffle=True)
    for i, fold in enumerate(kf):
        fold_data = {"train": [ int(msg_ids[x]) for x in fold[0] ], 
                     "test" : [ int(msg_ids[x]) for x in fold[1] ],
                     "val"  : [ int(msg_ids[x]) for x in fold[2] ] }
        with open(FOLDS + 'fold_%d.csv' % i, 'wb') as f: 
            w = csv.DictWriter(f, fold_data.keys())
            w.writeheader()
            w.writerow(fold_data)

print "Preprocess Data"
with codecs.open(TXT_OUT,"w","utf-8") as fod:
    with codecs.open(TXT_IN,"r","utf-8") as fid:
        msgs = []            
        fid.readline()
        for line in fid:                
            st = line.replace("\r","").replace("\n","").split("\t")
            if len(st) != 4:
                set_trace()            
            tweet_id = int(st[0].replace("\"",""))
            idz.append(tweet_id)
            user = st[1]           
            label = st[2]
            m = st[3]
            m = preprocess(m, sep_emoji=True)              
            m = m.replace("#sarcasm", "").replace("#sarcastic", "")
            m = m.replace("\"", "").replace("'","")    
            fod.write(u"%d\t%s\t%s\t%s\n" % (tweet_id,user,label,m))
            msgs.append(m)
#compute word index
wrd2idx = word_2_idx(msgs)    
print "Load Word Embeddings"
emb_utils.save_embeddings_txt(EMB_PATH_IN, EMB_PATH_OUT, wrd2idx)
build_folds(idz)



