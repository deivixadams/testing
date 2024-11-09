from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Que bien funciona esta vaina"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
