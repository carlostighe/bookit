from bookit import bookit as app
from livereload import Server

#server = Server(app.run(debug=True))
#server = Server(app.wsgi_app)
# server.watch
#server.serve()
app.run(debug=True)