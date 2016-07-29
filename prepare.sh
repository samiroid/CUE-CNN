utils="/home1/04069/samir/work/dev/projects/utils/my_utils"
sarcasm_embeddings="/home1/04069/samir/work/dev/resources/embeddings/sarcasm/"
mkdir DATA
mkdir DATA/embeddings
mkdir DATA/pkl
mkdir DATA/txt
rm code/my_utils
ln -s ${utils} code/my_utils
ln -s ${sarcasm_embeddings} DATA/embeddings/sarcasm
