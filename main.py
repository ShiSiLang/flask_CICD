from flask import Flask

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World...'


@app.route('/index/')
def index():
    return 'This is Index...'


@app.route('/user/<string:name>')
def user(name):
    return 'Hello ,{}...'.format(name)


@app.route('/post/<int:n>', methods=['POST'])
def post(n):
    return 'Hello , this is {}...'.format(n)


if __name__ == '__main__':
    app.run(debug=True)
