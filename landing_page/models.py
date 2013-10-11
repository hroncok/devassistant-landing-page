from landing_page import db

class FeedItem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)
    url = db.Column(db.Text)

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    snippet = db.Column(db.Text)
    full_text = db.Column(db.Text)
    importance = db.Column(db.Integer)
    active = db.Column(db.Boolean)

class MediaReference(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    snippet = db.Column(db.Text)
    orig_URL = db.Column(db.Text)
    orig_name = db.Column(db.Text)
    active = db.Column(db.Boolean)
