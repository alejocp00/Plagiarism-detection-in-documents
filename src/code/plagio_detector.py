from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel
import spacy

nlp = spacy.load('en_core_web_md')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def detect_plagiarism(text1, text2):
    similarity_ratio = compare_bert_embeddings(text1, text2)
    similarity_percentage = int(similarity_ratio * 100)
    return similarity_percentage

def compare_bert_embeddings(text1, text2):
    embedding1 = get_bert_embedding(text1)
    embedding2 = get_bert_embedding(text2)
    similarity = cosine_similarity([embedding1], [embedding2])[0][0]
    return similarity

def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()[0]




text1 = "Medicin is a field of bio that focuses on curing people capable of performing tasks that typically require human intelligence. These tasks include learning, reasoning, problem-solving, perception, and language understanding. AI systems can be categorized into two main types: narrow AI, which is designed to perform a narrow task (e.g., facial recognition, voice commands), and general AI, which is designed to understand, learn, and apply knowledge across a wide range of tasks. The development of AI has been driven by advancements in computing power, algorithms, and data storage. As AI technology continues to evolve, it is expected to have a significant impact on various industries, including healthcare, finance, and transportation."
tex2 = "Artificial intelligence is a branch of computer science that aims to develop systems that can carry out tasks that are typically associated with human intelligence. These tasks encompass learning, reasoning, problem-solving, perception, and understanding language. AI systems are generally classified into two main categories: narrow AI, which is engineered to execute a specific task (such as facial recognition or voice commands), and general AI, which is designed to comprehend, learn, and apply knowledge across a broad spectrum of tasks. The progress in AI has been propelled by improvements in computing power, algorithms, and data storage solutions. As AI technology advances, it is anticipated to influence numerous sectors, including healthcare, finance, and transportation."

sim = detect_plagiarism(text1, tex2)

print (sim)