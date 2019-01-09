from gensim.models import KeyedVectors
import operator

# load embedding index
embed_path =  'path'
embeddings_index = KeyedVectors.load_word2vec_format(embed_path, binary=True)



"""
 define a function that checks the intersection between our vocabulary and the embeddings. It will output a list of out of vocabulary  (oov) words that we can use to improve our preprocessing
"""

def check_coverage(vocab, embedding_index):
    a = {} # stor match vocabs with embedding index
    oov = {} # stor words does't exists in embedding index
    k = 0
    i = 0
    for word in tqdm(vocab):
        try:
            a[word] = embeddings_index[word]
            k += vocab[word]
        except:
            oov[word] = vocab[word]
            i += vocab[word]
            pass
    print('Found embedding for {:.2%} of vocab'.format(len(a) / len(vocab)))
    print('Found embedding for {:.2%} of all test'.format(k / (k + i)))
    sorted_x = sorted(oov.items(), key=operator.itemgetter(1))[::-1]
    
    return sorted_x

# we should pass embeddings_index and our vocabs
oov = check_coverage(vocab,embeddings_index)
