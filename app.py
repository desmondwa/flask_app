from flask import Flask

app = Flask(__name__)

@app.route('/')
def your_mom():
    return '<h1>hey ya</h1>'