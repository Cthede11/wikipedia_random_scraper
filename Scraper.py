from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    links = get_links(url)
    random_link = random.choice(links)
    return render_template('templates/index.html', link=random_link)

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

if __name__ == "__main__":
    app.run(debug=True)