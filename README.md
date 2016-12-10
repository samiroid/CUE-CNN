CUE-CNN
=======

Code for the sarcasm detection system described in the paper *Modelling Context with User Embeddings for Sarcasm Detection in Social Media* [[paper] (https://arxiv.org/abs/1607.00976)] [[bib] ()]

The CNN implemention was forked from [Giuseppe Attardi] (https://github.com/attardi/CNN_sentence) (which was forked from [Yoon Kim] (https://github.com/yoonkim/CNN_sentence))

pre-requisites:

* my_utils -> https://github.com/samiroid/utils
* pre-trained word embeddings (e.g. Skip-gram)
* user embeddings -> The embeddings we used can be found [here](https://www.dropbox.com/s/pmp5x08v6w09jrq/usr2vec_400_master.txt?dl=0). If you want to train your own embeddings you can use the code available [here](https://github.com/samiroid/usr2vec). 

requirements:
* python >= 2.7
* numpy
* theano

## Getting the data
To comply with Twitter policies we can only share the msg ids. These can be found in the file `bamman_redux_ids.txt`

## Running the code

1. clone or download the [my_utils] (https://github.com/samiroid/utils) module and place it under the folder `code`
2. run `juptyer notebook`; execute notebook `notebook.ipynb`
