from flask import Flask, make_response, redirect

app = Flask(__name__)

'''
@app.route('/')
def hello_world():
    return 'Hello nana!'

@app.route('/user/<name>')
def user(name):
    return ('<h1>hello:{0}!!</h1>').format(name),200



if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    response=make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
    
'''

@app.route('/')
def index():
    return redirect('http://www.example.com')
