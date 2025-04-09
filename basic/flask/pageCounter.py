from flask import Flask

app = Flask(__name__)
counter = 0

@app.route('/')
def home():
    global counter
    counter += 1
    return f"<h1>This page has been visited {counter} times.</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    