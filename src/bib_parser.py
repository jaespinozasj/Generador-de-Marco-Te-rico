import bibtexparser

def parse_bib_to_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    articles = []
    for entry in bib_database.entries:
        article = {
            "title": entry.get('title', ''),
            "authors": entry.get('author', ''),
            "year": entry.get('year', ''),
            "journal": entry.get('journal', ''),
            "volume": entry.get('volume', ''),
            "number": entry.get('number', ''),
            "pages": entry.get('pages', ''),
            "doi": entry.get('doi', ''),
            "abstract": entry.get('abstract', ''),
            "keywords": entry.get('keywords', '')
        }
        articles.append(article)
    
    return articles