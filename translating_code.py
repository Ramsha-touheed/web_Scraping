from bs4 import BeautifulSoup
import requests

def translate_html_file(file_path, from_language, to_language):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    elements = ['span','h1','h2','h3','h4','h5','h6''p','a','strong']
    for i in soup.findAll(elements):
        text = i.string
        if text is not None:
            translated_text = translate_text(text, from_language, to_language)
            i.string.replace_with(translated_text)

    with open(file_path, 'w') as file:
        file.write(str(soup))

def translate_text(text, from_language, to_language):
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl={from_language}&tl={to_language}&dt=t&q={text}'
    response = requests.get(url)
    response_json = response.json()
    translated_text = response_json[0][0][0]
    return translated_text
  
  
  
file_path = '/content/index.html'
translate_html_file(file_path, 'en', 'hi')
