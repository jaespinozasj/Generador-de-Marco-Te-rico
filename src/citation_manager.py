def create_apa_reference(article):
    authors = article['authors'].replace(' and ', ', ')
    title = article['title'].rstrip('.')
    journal = article['journal']
    volume = article['volume']
    pages = article['pages'].replace('--', '-')
    doi = article['doi']

    reference = f"{authors}. ({article['year']}). {title}. "
    if journal:
        reference += f"{journal}"
        if volume:
            reference += f", {volume}"
        if pages:
            reference += f", {pages}"
    reference += f". https://doi.org/{doi}" if doi else "."
    
    return reference