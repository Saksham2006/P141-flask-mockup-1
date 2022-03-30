from flask import Flask, request, jsonify
import csv

from itsdangerous import json

all_articles = []

liked_articles = []
not_liked_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

app = Flask(__name__)

@app.route('/get-article')
def get_article():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route('/liked-articles')
def liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status" : "success"
    }), 201

@app.route('/unliked-articles')
def unliked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()