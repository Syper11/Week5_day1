from app import app
from flask import render_template

@app.route('/')
@app.route('/Home')
def homepage():
    favorite = ['Sport Favorites']
    text = "To my top 5 picks!!"
    return render_template('index.html', favorite = favorite, my_text = text)

@app.route('/sports_figures')
def sports_figures():
    sport_fig = ['Michael Jordan','Jeff Gordon','Tom Brady','Pablo Sanchez','Jared Allen']
    return render_template('favorite_5.html', sport_fig = sport_fig)