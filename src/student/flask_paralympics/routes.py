from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Paralympics app'


@app.route('/paralympics')
def paralympics():
    return render_template('paralympics.html')


if __name__ == '__main__':
    app.run(debug=True)
