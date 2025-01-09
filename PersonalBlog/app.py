from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)

app.secret_key = "sarbesh" 
ADMIN_USERNAME = "sarbesh"
ADMIN_PASSWORD = "sarbesh123"

def load_articles():
    base_dir = os.path.dirname(__file__)  # Get the directory of the current script
    file_path = os.path.join(base_dir, 'articles.json')  # Construct the full path
    with open(file_path,'r') as file:
        return json.load(file)
    

@app.route('/')

def main():
    return redirect(url_for('about'))  # Redirect to the 'about' page


@app.route('/about')

def about():
    return render_template('about.html', logged_in=session.get("logged_in", False))    


@app.route('/home')

def home():
    articles = load_articles()

    # Pass logged_in status to template

    return render_template("home.html", articles=articles, logged_in = session.get("logged_in", False))

    #session.get("logged_in", False) --> will return value of key "logged_in" in session dictionary.
    #If key is not present, it will return False.


@app.route('/login',methods=['POST','GET'])

def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

            session["logged_in"] = True # Set the logged_in key in session dictionary to True

            return redirect(url_for('home')) # Redirect to main page
        
        else:
            return "Invalid credentials. Please try again."


@app.route('/logout')

def logout(): #will learn js later to add confirmation alert.

    # Remove the logged_in key from the session
    session.pop("logged_in", None)  # This will log out the user by clearing the session

    # Redirect to the home page or about page after logout
    return redirect(url_for('about'))  # Or redirect to 'home' or any other page you'd like


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
    return render_template("article.html", article=article, logged_in=session.get("logged_in", False))



if __name__ == '__main__':
    app.run(debug=True)