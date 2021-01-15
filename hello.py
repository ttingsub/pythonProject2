from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Pythonf web'

@app.route('/about')
def about():
    return 'about page'

@app.route('/login')
def login():
    return 'underconstuction'


    app.run()