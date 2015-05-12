from datetime import datetime
from flask import render_template, url_for, request
from bookit import bookit as app
from models import User

bookmarks = []

def store_bookmarks(url):
    bookmarks.append(dict(
        url = url,
        user = 'Carlos',
        date = datetime.utcnow()
        ))

@app.route('/')
def index():
    return render_template('index.html',
                           title='bookit!',
                           headline='When you see a site you like, bookit!',
                           user=User('Carlos', 'Tighe')
                           )

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmarks(url)
        app.logger.debug('stored url: ' + url)
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
