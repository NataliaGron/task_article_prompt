from openai import OpenAI
client = OpenAI(api_key='<API_KEY>')

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html_article(article_text):

    prompt = f"""
        Przekształć poniższy artykuł do struktury HTML.
        Użyj odpowiednich tagów HTML do strukturyzacji treści.
        Kod powinien znajdować się w tagu <article>.
        Zidentyfikuj miejsca, gdzie warto wstawić grafiki i oznacz je tagiem <img src="image_placeholder.jpg" alt="<prompt>">.
        Niech prompt będzie bardzo dokładny, aby można go było użyć do wygenerowania grafiki.
        Najlepiej, aby zaczynał się od słów: "Ilustracja przedstawiająca".
        Dodaj podpisy pod obrazkami z użyciem tagu <figcaption>.
        Proszę, aby wynik zawierał tylko część HTML, bez nagłówków <html>, <head> czy <body>.
        Wygeneruj to jako plain text a nie w bloku code.
        Treść artykułu:
        {article_text}
        """

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    a = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            a = a + (chunk.choices[0].delta.content)
    return a

def save_html_article(html_content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def main():
    article = 'article.txt'
    article_text = read_article(article)
    html_content = generate_html_article(article_text)
    save_html_article(html_content, 'artykul.html')

main()