from flask import Flask, render_template, request, redirect, url_for
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)
current_page = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_page
            
    if request.method == 'POST':
            if 'randomize' in request.form:  # "Randomize" button
                links, _ = get_links(current_page)
                random_link = random.choice(links) if links else ''
                current_page = random_link
                
            else:
                current_page = request.form.get('url')

    # Fetch title after setting the new current_page
    if current_page:
        _, title = get_links(current_page)

    else:  # Watch for Empty URL
        title = ''

    return render_template('index.html', link=current_page, title=title)

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content_div = soup.find('div', id='mw-content-text')

    links = [a['href'] for a in content_div.find_all('a', href=True) if a['href'].startswith('/wiki/')
        if a['href'].startswith('/wiki/') and ':' not in a['href']]
    
    links = ['https://en.wikipedia.org' + link for link in links]
    random.shuffle(links)
    title = soup.find('title').text
    return links, title

if __name__ == "__main__":
    app.run(debug=True)