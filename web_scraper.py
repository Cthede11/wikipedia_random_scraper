from flask import Flask, render_template, request, redirect, url_for
from bs4 import BeautifulSoup
import random
import requests

app = Flask(__name__)
visited_links = []
current_page = None

@app.route('/', methods=['GET', 'POST'])
def scrape_wikipedia():
    global visited_links, current_page
    if request.method == 'POST':
        start_url = request.form.get('start_url')
        current_page = start_url
        visited_links = [start_url]
        page_title = get_page_title(start_url)
        return render_template('index.html', page_title=page_title)
    return render_template('index.html')

@app.route('/navigate', methods=['GET'])
def navigate_page():
    global current_page
    return redirect(current_page)

@app.route('/randomize', methods=['POST'])
def randomize_page():
    global visited_links, current_page
    response = requests.get(current_page)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')
    links = [link for p in paragraphs for link in p.find_all('a', href=lambda href: href and href.startswith('/wiki/'))]
    random.shuffle(links)

    if links:
        random_link = links[0]
        next_url = 'https://en.wikipedia.org' + random_link['href']
        visited_links.append(next_url)  # Add the link to the visited_links list
        current_page = next_url
        page_title = get_page_title(next_url)
        return render_template('index.html', page_title=page_title)

def get_page_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

if __name__ == "__main__":
    app.run(debug=True)