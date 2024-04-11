from nltk.tokenize import word_tokenize, sent_tokenize


def preprocess_text(query):
    """
    Args:
        query (str): The input query to be preprocessed.

    Returns:
        list: The corpus?.
    """
    query = query.lower()
    paragraphs = convert_to_paragraphs(query)

    tokenized_words = [word_tokenize(sentence) for sentence in paragraphs]

    return tokenized_words


def convert_to_paragraphs(text):
    """
    Args:
        text (str): The input text to be converted to paragraphs.

    Returns:
        list: The list of paragraphs.
    """
    paragraphs = []
    tokens = sent_tokenize(text)
    for line in tokens:
        paragraphs.append(line)

    return paragraphs
