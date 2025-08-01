from flask import Flask, render_template, request
from trends_fetcher import get_related_queries
from routes.trending import trending_bp  #  blueprint routes
from routes.analyzer import analyzer_bp # blueprint routes
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

app = Flask(__name__)
app.register_blueprint(trending_bp)
app.register_blueprint(analyzer_bp)

@app.route('/', endpoint='index')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
