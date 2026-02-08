from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "ERROR404 in progres..."

if __name__ == '__main__':
    app.run(debug=True)
