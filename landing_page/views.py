from flask import render_template
from landing_page import app
import helpers
import models

@app.route("/")
def index():
    posts = models.FeedItem.query.all()
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/download")
def download():
    return render_template('download.html')

@app.route("/refreshrss")
def refreshrss():
    try:
        helpers.refresh_rss('http://blog.devassistant.org/?feed=rss2')
    except:
        return 'Failed'
    return 'Passed'

@app.route("/faq")
def faq():
    return render_template('faq.html')

@app.route("/contribute")
def contribute():
    return render_template('contribute.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/getstarted")
def getstarted():
    return render_template('getstarted.html')
