from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from datetime import date

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template(
        'index.html',
        current_date=date.today().year
    )


@app.route('/bootstrap')
def bootstrap_page():
    return render_template(
        'index-bootstrap.html',
        current_date=date.today().year
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
