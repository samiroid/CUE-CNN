CUE-CNN
=======

Code for the sarcasm detection system described in the paper *Modelling Context with User Embeddings for Sarcasm Detection in Social Media* [[paper] (https://arxiv.org/abs/1607.00976)] [[bib] ()]

The CNN implemention was forked from this [repo] (https://github.com/attardi/CNN_sentence) (which was forked this [repo] (https://github.com/yoonkim/CNN_sentence))

pre-requisites:

* my_utils -> https://github.com/samiroid/utils
* pre-trained word embeddings (e.g. Skip-gram)
* user embeddings -> The embeddings we used can be found [here](). If you want to train your own embeddings you can use the code available [here](https://github.com/samiroid/usr2vec). 

requirements:
* python >= 2.7
* numpy
* theano

## Getting the data
To comply with Twitter policies we can only share the msg ids. These can be found in the file `bamman_redux_ids.csv`

## Running the code

1. clone or download the [my_utils] (https://github.com/samiroid/utils) module and place it under the folder `code`
2. run `prepare.sh` with the paths to the utils module and the word embeddings: `./prepare.sh PATH_TO_WORD_EMBEDDINGS PATH_TO_USER_EMBEDDINGS`
3. run `sarcasm_cnn.sh` 

## Replicating the results from the paper
4. run `crossfolds.sh`

