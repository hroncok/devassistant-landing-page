from flask import render_template
from landing_page import app
import helpers
import models

@app.route("/login")
def login():
    posts = models.FeedItem.query.all()
    return render_template('index.html', posts=posts)
