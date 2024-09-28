from openai import OpenAI

def prepare_llm_prompt(cluster_summaries, topic, key_concepts=None, writing_style="formal", max_words=1000):
    prompt = f"Generar un {writing_style} marco teórico de aproximadamente {max_words} palabras sobre el tema de '{topic}' basado en los siguientes resúmenes de grupos de investigación:\n\n"
    for i, summary in cluster_summaries.items():
        prompt += f"Cluster {i}:\n{summary}\n\n"
    
    if key_concepts and key_concepts[0]:  # Check if key_concepts is not empty
        prompt += f"Asegúrese de incluir y discutir los siguientes conceptos clave: {', '.join(key_concepts)}\n\n"
    
    prompt += "Instrucciones:\n"
    prompt += "1. Identifica los temas principales en todos los grupos relacionados con el tema dado.\n"
    prompt += "2. Explica cómo estos temas están interconectados, utilizando citas en el texto.\n"
    prompt += "3. Destaca cualquier contradicción o laguna en la investigación actual.\n"
    prompt += "4. Propone un marco teórico coherente que sintetice estos hallazgos.\n"
    prompt += "5. Sugiere posibles áreas para futuras investigaciones basadas en este marco.\n"
    prompt += "6. Utiliza citas apropiadas en el texto a lo largo del marco.\n"
    prompt += "7. No incluyas una lista de referencias al final del marco.\n"
    
    return prompt

def send_to_llm_api(client, prompt, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Eres un asistente en español útil que genera marcos teóricos basados en investigaciones académicas."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.7
    )
    return response.choices[0].message.content

def generate_research_questions(client, cluster_summaries, topic, n_questions=5):
    prompt = f"Basado en los siguientes resúmenes de investigación sobre '{topic}', genera {n_questions} posibles preguntas de investigación para futuras investigaciones:\n\n"
    for i, summary in cluster_summaries.items():
        prompt += f"Cluster {i}:\n{summary}\n\n"
    
    prompt += f"Por favor enumera {n_questions} preguntas de investigación distintas que aborden lagunas o amplíen la investigación actual sobre {topic}."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente en español útil que genera preguntas de investigación basadas en literatura académica."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    
    return response.choices[0].message.content