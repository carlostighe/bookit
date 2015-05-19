from bookit import bookit as app, db
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
#@manager.command makes commands available on command line
def initdb():
    db.create_all()
    print 'Creating the database....'
    print '...'
    print '...'
    print '...'
    print 'Initialised the database....'

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