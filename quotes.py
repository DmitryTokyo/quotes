from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from environs import Env

env = Env()
env.read_env()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env('SQLALCHEMY_TRACK_MODIFICATIONS')

db = SQLAlchemy(app)


class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    results = Favquotes.query.all()
    return render_template('index.html', results=results)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))