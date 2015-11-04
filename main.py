#!/usr/bin/python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return '<p>Hello, %s.<p>' % name

if __name__ == '__main__':
	app.run(debug=True)
