from flask import Blueprint, render_template, request
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

analyzer_bp = Blueprint('analyzer', __name__, template_folder='../templates')

STOPWORDS = set([
    'the', 'and', 'to', 'of', 'in', 'a', 'is', 'for', 'on',
    'with', 'that', 'by', 'as', 'at', 'an', 'it', 'this', 'be'
])

@analyzer_bp.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        url = request.form['url'].strip()

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"ERROR: {e}")
            return render_template('analyze.html', error="❌ Failed to analyze the URL. Check format and try again.")

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        words = re.findall(r'\b\w+\b', text.lower())
        filtered_words = [w for w in words if w not in STOPWORDS and len(w) > 2]
        word_counts = Counter(filtered_words).most_common(10)

        h1 = len(soup.find_all('h1'))
        h2 = len(soup.find_all('h2'))
        h3 = len(soup.find_all('h3'))

        total_words = len(filtered_words)
        reading_time = round(total_words / 200, 2)

        return render_template('results.html', url=url,
                               word_counts=word_counts,
                               h1=h1, h2=h2, h3=h3,
                               total_words=total_words,
                               reading_time=reading_time)

    return render_template('analyze.html')
