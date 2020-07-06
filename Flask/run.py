from flask import jsonify
from flask import request
from flask import Flask
from MySQLCommand import MySQLCommand


app=Flask(__name__)

@app.route('/')
def hello():
    return "hi"

app.run(debug=False)