from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_relevance_scores(articles, query):
    texts = [f"{a['title']} {a['abstract']} {a['keywords']}" for a in articles]
    texts.append(query)
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    scores = (cosine_similarities[0] - np.min(cosine_similarities[0])) / (np.max(cosine_similarities[0]) - np.min(cosine_similarities[0]))
    
    return list(scores)