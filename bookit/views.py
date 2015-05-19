from datetime import datetime
from flask import render_template, url_for, request, redirect, flash
from bookit import bookit as app, db
from models import User, Bookmark
from forms import BookmarkForm

def logged_in_user():
    carlos = User.query.filter_by(username="Carlos").first()
    if(carlos):
        return carlos
    else:
        user = User(username="Carlos", email="carlos@example.com");
        db.session.add(user)
        db.session.commit()
        return user

def store_bookmarks(url, description):
    bookmarks.append(dict(
        url = url,
        description=description,
        user = 'Carlos',
        date = datetime.utcnow()
        ))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='bookit!',
                           headline='When you see a site you like, bookit!',
                           new_bookmarks=Bookmark.newest(5)
                           )

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(user=logged_in_user(), url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        #app.logger.debug('stored url: ' + url)
        #app.logger.debug(request.headers)
        flash("Stored bookmark '{}'".format(description))
        return redirect(url_for('index'))

    return render_template('add.html', form=form)

@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
