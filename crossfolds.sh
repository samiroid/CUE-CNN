#fold 1
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_1.csv -context 1

#fold 2
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_2.csv -context 1

#fold 3
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_3.csv -context 1

#fold 4
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_4.csv -context 1

#fold 5
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_5.csv -context 1

#fold 6
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_6.csv -context 1

#fold 7
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_7.csv -context 1

#fold 8
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_8.csv -context 1

#fold 9
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_9.csv -context 1

#fold 10
python code/crossfold_run.py DATA/pkl/cross.pkl DATA/txt/bamman_clean.txt -idField 0 -userField 1 -tagField 2 -textField 3 -vectors DATA/embeddings/filtered_embs.txt -user_vectors DATA/embeddings/usr2vec.txt -folds DATA/folds/fold_10.csv -context 1
