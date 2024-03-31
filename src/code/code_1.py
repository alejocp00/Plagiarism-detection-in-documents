import nltk
import gensim
from preprocess import preprocess_query


def plagio_between_docs(doc1, doc2):
    # Preprocess the documents
    p_doc1 = preprocess_query(doc1)
    p_doc2 = preprocess_query(doc2)

    print(type(p_doc2))

    # Calculate the cosine similarity
    p_doc1 = gensim.matutils.corpus2dense([p_doc1], num_terms=len(set(p_doc1)), num_docs=1).T
    p_doc2 = gensim.matutils.corpus2dense([p_doc2], num_terms=len(set(p_doc2)), num_docs=1).T
    similarity = gensim.similarities.cosine_sim(p_doc1, p_doc2)
    
    # Calculate the percentage of plagiarism
    plagiarism_percentage = similarity / 1.0 * 100
    
    # Identify the sections of the text where the plagiarism occurs
    plagiarized_sections = []
    for i in range(len(p_doc1)):
        if p_doc1[0][i] == p_doc2[0][i]:
           plagiarized_sections.append(p_doc1[0][i])

    # Print the results
    print(f"The percentage of plagiarism is {plagiarism_percentage}%")
    print("Plagiarized sections:")
    for section in plagiarized_sections:
        print(f"- {section}")

def calculate_similarity(doc_index, query_vector):

    # Calcular el valor promedio de la correlación
    t_i_j = sum(sum(row) for row in correlation_matrix) / n

    # Calcular la similitud del coseno entre el vector del documento y el vector de la consulta
    return cosine_similarity([weight_doc_matrix[doc_index]], [query_vector])[0][0]*t_i_j




# import gensim

# Define the documents
doc1 = "this is the first document"
doc2 = "this is the second ocument"

plagio_between_docs(doc1, doc2)

# # Calculate the number of unique terms in the corpus
# num_terms = len(set(doc1 + doc2))

# # Convert the documents to a bag-of-words representation
# bow_doc1 = gensim.corpora.Dictionary([doc1]).doc2bow()
# bow_doc2 = gensim.corpora.Dictionary([doc2]).doc2bow()

# # Convert the bag-of-words representation to a dense matrix
# doc1 = gensim.matutils.corpus2dense([bow_doc1], num_terms=num_terms, num_docs=1).T
# doc2 = gensim.matutils.corpus2dense([bow_doc2], num_terms=num_terms, num_docs=1).T

# # Calculate the cosine similarity
# similarity = gensim.similarities.cosine_sim(doc1, doc2)

# # Print the similarity score
# print(similarity[0][0])
    