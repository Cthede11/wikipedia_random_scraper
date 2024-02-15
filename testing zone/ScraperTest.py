from flask import Flask, render_template, request, redirect, url_for, session
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)
app.secret_key = '1234ABCD'
current_page = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_page
            
    if request.method == 'POST':
        if 'randomize' in request.form:  # "Randomize" button
            links, _ = get_links(current_page)
            random_link = random.choice(links) if links else ''
            current_page = random_link

        # add elif section to detect if a link in past pages was clicked
                
        else:
            current_page = request.form.get('url')

    past_pages = session.get('past_pages', [])

    # Fetch title after setting the new current_page
    if current_page:
        _, title = get_links(current_page)
        # Update the list of past pages
        past_pages = session.get('past_pages', [])
        past_pages.append(current_page)
        session['past_pages'] = past_pages[-4:]  # Keep only the last 5 pages
    else:  # Watch for Empty URL
        title = 'Unknown or Missing Page Title'

    return render_template('index.html', link=current_page, title=title, past_pages=past_pages)

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