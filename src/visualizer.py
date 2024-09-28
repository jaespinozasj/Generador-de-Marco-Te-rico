import networkx as nx
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

def visualize_article_network(articles, tfidf_matrix):
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    G = nx.Graph()
    
    for i, article in enumerate(articles):
        G.add_node(i, title=article['title'])
    
    for i in range(len(articles)):
        for j in range(i+1, len(articles)):
            if similarity_matrix[i][j] > 0.2:  # Umbral de similitud
                G.add_edge(i, j, weight=similarity_matrix[i][j])
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=False, node_color='lightblue', node_size=500, font_size=8)
    nx.draw_networkx_labels(G, pos, {i: G.nodes[i]['title'][:20] + '...' for i in G.nodes()})
    plt.title("Red de Relaciones entre Artículos")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('article_network.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("La visualización de la red de artículos ha sido guardada como 'article_network.png'")