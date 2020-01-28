from bookit import create_app
from livereload import Server

# server = Server(app.run(debug=True))
# server = Server(app.wsgi_app)
# server.watch
# server.serve()
app = create_app("dev")
app.run(debug=True,  host='0.0.0.0')
