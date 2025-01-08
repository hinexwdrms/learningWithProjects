from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)

def load_articles():
    with open('articles.json','r') as file:
        return json.load(file)
    

@app.route('/')

def main():
    return render_template('main.html')

@app.route('/about')

def about():
    return render_template('about.html')    

@app.route('/home')

def home():
    articles = load_articles()
    return render_template('home.html', articles=articles)

@app.route('/login',methods=['POST','GET'])

def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        pass

@app.route("/article/<int:article_id>") # This is a dynamic route that accepts an integer as an argument

def view_article(article_id): # The argument is passed to the function
    # Load articles from the JSON file
    articles = load_articles()
    
    # Find the article by its ID
    article = next((a for a in articles if a["id"] == article_id), None)
    
    # If the article doesn't exist, return a 404 page
    if not article:
        return "Sorry we encountered some error while fetching the article. 404"

    # Render the article page
    return render_template("article.html", article=article)

if __name__ == '__main__':
    app.run(debug=True)