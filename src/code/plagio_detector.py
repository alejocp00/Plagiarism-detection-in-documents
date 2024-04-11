import gensim
from src.code.preprocess import preprocess_text, convert_to_paragraphs


class Plagiarism:

    def __init__(self) -> None:
        self.max_sim = []
        self.path = []

    def detect_plagiarism(self, text1, text2):
        """
        Compara dos piezas de texto y calcula su similitud.

        Parámetros:
        - text1: Primera pieza de texto.
        - text2: Segunda pieza de texto.

        Retorna:
        - Un porcentaje de similitud entre 0 y 100.
        """
        # Preprocesar los textos
        text1_processed = preprocess_text(text1)
        dictionary = gensim.corpora.Dictionary(text1_processed)
        corpus = [dictionary.doc2bow(sent) for sent in text1_processed]

        tf_idf = gensim.models.TfidfModel(corpus)
        sims = gensim.similarities.Similarity(
            "./src/code/simObjectDir/", tf_idf[corpus], num_features=len(dictionary)
        )

        self.path = text2
        text2_processed = preprocess_text(text2)
        similarity = []
        for line in text2_processed:
            query_doc_bow = dictionary.doc2bow(line)
            query_doc_tf_idf = tf_idf[query_doc_bow]
            similarity.append(query_doc_tf_idf)

        vectors = [sims[vec] for vec in similarity]

        self.max_sim = [max(ind) for ind in vectors]

        similarity_percentage = int(sum(self.max_sim) / len(self.max_sim) * 100)

        return similarity_percentage

    def most_similar_path(self):
        max_path = [
            index_max
            for index_max, value in enumerate(self.max_sim)
            if value == max(self.max_sim)
        ].pop()

        path = convert_to_paragraphs(self.path)

        return path[max_path]
