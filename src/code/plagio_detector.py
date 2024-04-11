
import gensim
from preprocess import preprocess_text

def detect_plagiarism(text1, text2):
    """
    Compara dos piezas de texto y calcula su similitud.
    
    Parámetros:
    - text1: Primera pieza de texto.
    - text2: Segunda pieza de texto.
    
    Retorna:
    - Un porcentaje de similitud entre 0 y 100.
    - Una lista de operaciones que describen cómo transformar el primer texto en el segundo.
    """
    # Preprocesar los textos
    text1_processed = preprocess_text(text1)
    dictionary = gensim.corpora.Dictionary(text1_processed)
    corpus = [dictionary.doc2bow(sent) for sent in text1_processed]

    tf_idf = gensim.models.TfidfModel(corpus)
    sims = gensim.similarities.Similarity('simObjectDir/', tf_idf[corpus], num_features=len(dictionary))

    
    text2_processed = preprocess_text(text2)
    similarity = []
    for line in text2_processed:
        query_doc_bow = dictionary.doc2bow(line)
        query_doc_tf_idf = tf_idf[query_doc_bow]
        similarity.append(query_doc_tf_idf)

    max_sim = [ max(ind) for ind in similarity]
    # similarity_percentage = int((sum(max_sim)/ len(max_sim)) * 100)

    return max_sim
