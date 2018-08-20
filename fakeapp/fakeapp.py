from flask import Flask

app = Flask('fakeapp')


@app.route('/')
def home():
    return "fake app v0.3.0"
