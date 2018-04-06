from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Index'

@app.route("/hello")
def hello():
    return 'Hello world!'

@app.route("/members")
def members():
    return 'members'

@app.route("/members/<string:name>/")
def getMember(name):
    return name


if __name__ == '__main__':
    app.run()
