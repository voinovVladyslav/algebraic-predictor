from flask import render_template
from . import main


@main.route('/', endpoint='home')
def home():
    return render_template('home.html')


@main.route('/api/docs', endpoint='api_docs')
def api():
    return render_template('api_docs.html')
