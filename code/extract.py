import cPickle
import csv
from my_utils import preprocess
from my_utils import embeddings as emb_utils
from my_utils import word_2_idx
from my_utils import kfolds
import pprint
from pdb import set_trace

EMB_PATH_IN = "DATA/embeddings/sarcasm/sarcasm_embeddings_400.txt"
FILTERED_EMBEDDINGS = "DATA/embeddings/filtered_embs.txt"
BAMMAN_RAW = "DATA/txt/experiment.csv"
BAMMAN_CLEAN = "DATA/txt/bamman_clean.txt"
PKL = "DATA/pkl/sarcasm.pkl"
FOLDS =  "DATA/folds/"
idz = []

import codecs
with codecs.open(BAMMAN_CLEAN,"w","utf-8") as fod:
    with codecs.open(BAMMAN_RAW,"r","utf-8") as fid:
        msgs = []            
        fid.readline()
        for line in fid:                
            st = line.replace("\r","").replace("\n","").split(",")
            if len(st) != 4:
                set_trace()
            tweet_id = int(st[0].replace("\"",""))
            idz.append(tweet_id)
            user = st[2]           
            label = st[3]
            # m = ' '.join(st[4:])
            m = st[1]
            m = preprocess(m)        
            # m = preprocess(m)        
            m = m.replace("#sarcasm", "").replace("#sarcastic", "")
            m = m.replace("\"", "").replace("'","")      
            # fod.write("%d\t%s\t%s\t%s\n" % (tweet_id,user,label,m.encode("utf-8")))
            fod.write(u"%d\t%s\t%s\t%s\n" % (tweet_id,user,label,m))
            # fod.write("%s\t%s\t%s\n" % (user,st[1],m))
            msgs.append(m)
# set_trace()
#build vocabulary        
wrd2idx = word_2_idx(msgs)    
emb_utils.save_embeddings_txt(EMB_PATH_IN, FILTERED_EMBEDDINGS, wrd2idx)
E = emb_utils.get_embeddings(EMB_PATH_IN, wrd2idx)

with open(PKL,"wb") as fid:
    cPickle.dump([E,wrd2idx], fid)

# kf = kfolds(10, len(idz),val_set=True,shuffle=True)

# for i, fold in enumerate(kf):
#     fold_data = {"train": [ int(idz[x]) for x in fold[0] ], 
#                  "test" : [ int(idz[x]) for x in fold[1] ],
#                  "val"  : [ int(idz[x]) for x in fold[2] ] }
#     with open(FOLDS + 'fold_%d.csv' % i, 'wb') as f: 
#         w = csv.DictWriter(f, fold_data.keys())
#         w.writeheader()
#         w.writerow(fold_data)

