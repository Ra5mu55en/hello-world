from flask import Flask, render_template, request, jsonify
from flask import make_response

app = Flask(__name__)


@app.route('/')
def home():
    return "hi"
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/addnumber')
def add():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return jsonify(result=a + b)

if __name__ == "__main__":
    app.run(debug = True)
