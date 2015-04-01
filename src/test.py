from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.tpl')

@app.route('/message')
def message():
    return '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.'''

@app.route('/_add')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/p/<name>')
def page(name=None):
    return render_template('hello.tpl', name=name)

if __name__ == '__main__':
    app.run()