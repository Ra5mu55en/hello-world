from werkzeug.exceptions import HTTPException
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

sentry_sdk.init(
    ignore_errors=[HTTPException]  # workaround to ignore abort() on inside flask-restful
)

@app.route('/')
def index():
    alert('In index')
    return render_template('index.html')

@app.route('/submit')
def submit():
    alert('In submit')
    return "Nothing"



if __name__ == '__main__':
   app.run()
