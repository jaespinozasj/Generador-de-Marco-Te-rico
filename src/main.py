import os
from dotenv import load_dotenv
from openai import OpenAI
import yaml
from bib_parser import parse_bib_to_json
from preprocessor import preprocess_articles, cluster_articles, prepare_cluster_summary
from llm_interface import prepare_llm_prompt, send_to_llm_api, generate_research_questions
from citation_manager import create_apa_reference
from relevance_scorer import calculate_relevance_scores
from visualizer import visualize_article_network

# Cargar variables de entorno
load_dotenv()

def load_config():
    with open('config/config.yml', 'r') as file:
        return yaml.safe_load(file)

def save_to_markdown(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("Iniciando el generador de marco teórico...")
    config = load_config()
    print("Configuración cargada.")
    
    # Configurar OpenAI API
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    if not client.api_key:
        raise ValueError("No se encontró la clave API de OpenAI. Asegúrate de que esté en el archivo .env")
    print("API de OpenAI configurada.")
    
    # Cargar y procesar datos
    print("Cargando artículos...")
    articles = parse_bib_to_json(config['input_file'])
    print(f"{len(articles)} artículos cargados.")
    
    print("Preprocesando artículos...")
    tfidf_matrix = preprocess_articles(articles)
    print("Preprocesamiento completado.")
    
    # Obtener tema del usuario
    topic = input("Ingrese el tema principal para el marco teórico: ")
    
    print("Calculando puntuaciones de relevancia...")
    relevance_scores = calculate_relevance_scores(articles, topic)
    
    # Ordenar artículos por relevancia
    sorted_articles = [article for _, article in sorted(zip(relevance_scores, articles), key=lambda x: x[0], reverse=True)]
    
    # Usar los N artículos más relevantes
    top_n = min(config['top_n_articles'], len(sorted_articles))
    top_articles = sorted_articles[:top_n]
    
    print(f"\nLos 5 artículos más relevantes son:")
    for i, article in enumerate(top_articles[:5], 1):
        print(f"{i}. \"{article['title']}\" ({article['year']})")
    
    print("\nAgrupando artículos...")
    clusters = cluster_articles(tfidf_matrix[:top_n], n_clusters=config['n_clusters'])
    cluster_summaries = prepare_cluster_summary(top_articles, clusters)
    print("Agrupación completada.")
    
    print("Generando visualización de la red de artículos...")
    visualize_article_network(top_articles, tfidf_matrix[:top_n])
    print("Visualización guardada como 'article_network.png'")
    
    # Obtener entrada del usuario para la generación del marco
    key_concepts = input("Ingrese conceptos clave a incluir (separados por comas) o presione Enter para omitir: ").split(',') if input("¿Desea especificar conceptos clave? (s/n): ").lower() == 's' else []
    writing_style = input("Ingrese el estilo de escritura deseado (formal/accesible): ") or "formal"
    max_words = int(input("Ingrese el número máximo de palabras para el marco: ") or 1000)
    
    print("Preparando prompt para el modelo de lenguaje...")
    prompt = prepare_llm_prompt(cluster_summaries, topic, key_concepts, writing_style, max_words)
    
    print("Generando marco teórico...")
    theoretical_framework = send_to_llm_api(client, prompt, model=config['model'])
    
    print("Generando preguntas de investigación...")
    research_questions = generate_research_questions(client, cluster_summaries, topic)
    
    # Guardar el marco teórico en un archivo Markdown
    markdown_content = f"# Marco Teórico: {topic}\n\n{theoretical_framework}\n\n## Preguntas de Investigación Sugeridas\n\n{research_questions}\n\n## Referencias\n\n"
    for article in top_articles:
        markdown_content += f"{create_apa_reference(article)}\n"
    
    filename = f"marco_teorico_{topic.replace(' ', '_')}.md"
    save_to_markdown(markdown_content, filename)
    print(f"Marco teórico guardado en '{filename}'")
    
    print("\nProceso completado.")

if __name__ == "__main__":
    main()