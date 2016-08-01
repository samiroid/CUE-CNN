CUE-CNN
=======

Code for the sarcasm detection system described in the paper *Modelling Context with User Embeddings for Sarcasm Detection in Social Media* [[paper] (https://arxiv.org/abs/1607.00976)] [[bib] ()]

The CNN implemention was forked from this [repo] (https://github.com/attardi/CNN_sentence) (which was forked this [repo] (https://github.com/yoonkim/CNN_sentence))

prerequisites:

* my_utils -> https://github.com/samiroid/utils
* pre-trained word embeddings (e.g. Skip-gram)
* user embeddings -> The embeddings we used can be found [here](https://www.google.com). If you want to train your own embeddings you can use the code available [here](https://github.com/samiroid/usr2vec)

###Setup

1. clone or download the [my_utils] (https://github.com/samiroid/utils) module and place it under the folder **code**
2. run **prepare.sh** with the paths to the utils module and the word embeddings. e.g. ./prepare.sh _PATH_TO_UTILS_ _PATH_TO_EMBEDDINGS_

