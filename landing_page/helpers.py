from datetime import datetime
from feedparser import parse
from HTMLParser import HTMLParser
from itertools import islice
from landing_page import db
from models import FeedItem
from time import mktime
import re

def refresh_rss(url):
    feed = parse(url)
    if feed['bozo'] == 1:
        raise Exception, '%s is not a valid RSS stream!' % url

    items = []
    for item in islice(feed['items'], 5):
        feeditem = FeedItem(title=item.title,
                            description=re.sub('<[^<]+?>', '', HTMLParser().unescape(item.description)),
                            date=datetime.fromtimestamp(mktime(item.updated_parsed)),
                            url=item.link)
        items.append(feeditem)

    FeedItem.query.delete()
    db.session.add_all(items)
    db.session.commit()
