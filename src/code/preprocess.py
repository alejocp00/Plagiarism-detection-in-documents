
from nltk.tokenize import word_tokenize, sent_tokenize

def preprocess_text(query):
    """
    Args:
        query (str): The input query to be preprocessed.

    Returns:
        list: The corpus?.
    """
    query = query.lower()
    paragraphs = []
    tokens = sent_tokenize(query)
    for line in tokens:
        paragraphs.append(line)

    tokenized_words = [word_tokenize(sentence) for sentence in paragraphs]

    return tokenized_words


