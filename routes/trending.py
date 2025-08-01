from flask import Blueprint, render_template, request
from trends_fetcher import get_related_queries

trending_bp = Blueprint('trending', __name__)

@trending_bp.route('/trending', methods=['GET', 'POST'])
def trending():
    results = []
    keyword = ''
    if request.method == 'POST':
        keyword = request.form['keyword']
        results = get_related_queries(keyword)
    return render_template('trending.html', keyword=keyword, results=results)