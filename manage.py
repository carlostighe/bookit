from bookit import bookit as app, db
from bookit.models import User, Bookmark, Tag

from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
#@manager.command makes commands available on command line
@manager.command
def insert_data():
    print 'Creating the database....'
    carlos = User(username="carlos", email="carlos@example.com", password="carlos")
    db.session.add(carlos)
    print '...'
    def add_bookmark(url, description, tags):
        db.session.add(Bookmark(url=url, description=description, user=carlos,
                                tags=tags))

    for name in ["python", "flask", "webdev", "programming", "training", "news", "orm", "databases", "emacs", "gtd", "django"]:
        db.session.add(Tag(name=name))
    db.session.commit()
    print '...'
    add_bookmark("http://www.pluralsight.com", "Pluralsight. Hardcore developer training.", "training,programming,python,flask,webdev")
    add_bookmark("http://www.python.org", "Python - my favorite language", "python")
    add_bookmark("http://flask.pocoo.org", "Flask: Web development one drop at a time.", "python,flask,webdev")
    add_bookmark("http://www.reddit.com", "Reddit. Frontpage of the internet", "news,coolstuff,fun")
    add_bookmark("http://www.sqlalchemyorg", "Nice ORM framework", "python,orm,databases")

    arjen = User(username="arjen", email="arjen@robben.nl", password="arjen")
    db.session.add(arjen)
    db.session.commit()
    print 'Initialized the database'

@manager.command
def dropdb():
    if prompt_bool("Are you sure? You will lose all data"):
        db.drop_all()
        print 'Dropping the database...'
        print '...'
        print '...'
        print '...'
        print 'Dropped the database.....'

if __name__ == '__main__':
    manager.run()