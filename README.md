# Generador de Marco Teórico

Este proyecto genera un marco teórico basado en un conjunto de artículos académicos proporcionados en formato BibTeX, utilizando inteligencia artificial para sintetizar la información y crear un documento estructurado.

## Características

- Análisis de relevancia de artículos basado en un tema especificado
- Visualización de la red de relaciones entre artículos
- Generación de marco teórico personalizado utilizando GPT-4
- Generación de preguntas de investigación sugeridas
- Referencias en formato APA
- Conversión del marco teórico de Markdown a formato DOCX

## Requisitos previos

- Python 3.7 o superior
- Una cuenta de OpenAI con acceso a la API de GPT-4
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/theoretical-framework-generator.git
   cd theoretical-framework-generator
   ```

2. Crea un entorno virtual (opcional, pero recomendado):
   ```
   python -m venv .venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```
     .venv\Scripts\activate
     ```
   - En macOS y Linux:
     ```
     source .venv/bin/activate
     ```

4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

5. Crea un archivo `.env` en la raíz del proyecto con tu clave API de OpenAI:
   ```
   OPENAI_API_KEY=tu_clave_api_aquí
   ```

## Uso

1. Coloca tu archivo BibTeX en el directorio `data/` y nómbralo `input.bib`.

2. Ejecuta el script principal:
   ```
   python src/main.py
   ```

3. Sigue las instrucciones en pantalla para:
   - Ingresar el tema principal del marco teórico
   - Especificar conceptos clave (opcional)
   - Elegir el estilo de escritura
   - Definir la longitud máxima del marco teórico

4. El programa generará:
   - Una visualización de la red de artículos (guardada como 'article_network.png')
   - Un marco teórico sobre el tema especificado (en formato Markdown)
   - Preguntas de investigación sugeridas
   - Una lista de referencias en formato APA

5. Para convertir el marco teórico de Markdown a DOCX, ejecuta:
   ```
   python src/md_to_docx.py nombre_del_archivo_markdown.md
   ```
   Reemplaza `nombre_del_archivo_markdown.md` con el nombre real del archivo generado.

## Reinicio del proyecto

Si cierras Visual Studio Code o tu terminal y necesitas reiniciar el proyecto:

1. Abre una nueva terminal y navega al directorio del proyecto:
   ```
   cd ruta/a/theoretical-framework-generator
   ```

2. Activa el entorno virtual:
   - En Windows:
     ```
     .venv\Scripts\activate
     ```
   - En macOS y Linux:
     ```
     source .venv/bin/activate
     ```

3. Ahora puedes ejecutar los scripts como se describió anteriormente.

## Estructura del proyecto

```
theoretical_framework_generator/
│
├── data/
│   └── input.bib
│
├── src/
│   ├── __init__.py
│   ├── bib_parser.py
│   ├── preprocessor.py
│   ├── relevance_scorer.py
│   ├── visualizer.py
│   ├── llm_interface.py
│   ├── citation_manager.py
│   ├── main.py
│   └── md_to_docx.py
│
├── config/
│   └── config.yml
│
├── requirements.txt
├── .env
└── README.md
```

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios importantes antes de crear un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Descargo de responsabilidad

Este proyecto utiliza la API de OpenAI y está sujeto a sus términos de servicio. Asegúrate de cumplir con las políticas de uso de OpenAI al utilizar este software.

El marco teórico generado y las preguntas de investigación sugeridas deben ser revisados y editados por un humano antes de su uso en trabajos académicos.

## Exportación de datos desde bases de datos científicas

Antes de usar este generador de marco teórico, necesitas exportar los datos bibliográficos de tus artículos científicos en formato BibTeX (.bib). Aquí te explicamos cómo hacerlo desde algunas bases de datos comunes:

### Scopus

1. Realiza tu búsqueda en Scopus.
2. Selecciona los artículos que deseas incluir.
3. Haz clic en "Export".
4. En el menú desplegable, selecciona "BibTeX".
5. En la ventana emergente, asegúrate de marcar las siguientes opciones:
   - Citation information
   - Bibliographical information
   - Abstract & keywords
   - Funding details
6. Haz clic en "Export" y guarda el archivo .bib.

### Web of Science

1. Realiza tu búsqueda en Web of Science.
2. Selecciona los artículos que deseas incluir.
3. Haz clic en "Export".
4. Selecciona "BibTeX" como formato de archivo.
5. Asegúrate de que todas las opciones de campos están seleccionadas.
6. Haz clic en "Export" y guarda el archivo .bib.

### Google Scholar

Google Scholar no ofrece una opción directa para exportar múltiples referencias en formato BibTeX. Sin embargo, puedes usar una extensión de navegador como "Zotero Connector" para recopilar las referencias y luego exportarlas a BibTeX.

1. Instala la extensión Zotero Connector para tu navegador.
2. Realiza tu búsqueda en Google Scholar.
3. Usa la extensión para guardar las referencias en Zotero.
4. En Zotero, selecciona las referencias que deseas exportar.
5. Haz clic derecho y selecciona "Exportar elementos...".
6. Elige el formato BibTeX y guarda el archivo .bib.

### Campos importantes

Asegúrate de que tu archivo BibTeX incluya los siguientes campos para cada artículo (si están disponibles):

- Título (title)
- Autores (author)
- Año (year)
- Revista (journal)
- Volumen (volume)
- Número (number)
- Páginas (pages)
- DOI
- Resumen (abstract)
- Palabras clave (keywords)

Una vez que tengas tu archivo .bib, colócalo en la carpeta `data/` de este proyecto y nómbralo `input.bib`.
