from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def preprocess_articles(articles):
    texts = [f"{a['title']} {a['abstract']} {a['keywords']}" for a in articles]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    return tfidf_matrix

def cluster_articles(tfidf_matrix, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(tfidf_matrix)
    return kmeans.labels_

def prepare_cluster_summary(articles, clusters):
    summaries = {}
    for i in range(max(clusters) + 1):
        cluster_articles = [a for a, c in zip(articles, clusters) if c == i]
        summary = "Cluster Summary:\n"
        for article in cluster_articles[:3]:
            authors = article['authors'].split(' and ')
            if len(authors) > 1:
                citation = f"({authors[0].split(',')[0]} et al., {article['year']})"
            else:
                citation = f"({authors[0].split(',')[0]}, {article['year']})"
            summary += f"- {article['title']} {citation}: {article['abstract'][:100]}...\n"
        summaries[i] = summary
    return summaries