from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1>"

@app.route('/help')
def help():
    return "<h1>Help Page</h1>"

@app.route('/faq')
def faq():
    return "<h1>FAQ Page</h1>"

@app.route('/date')
def date():
    today = datetime.date.today()
    return f"<h1>Today's date is {today}</h1>"

if __name__ == '__main__':
    app.run(debug=True)