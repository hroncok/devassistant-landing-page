from ConfigParser import SafeConfigParser
from datetime import datetime
from feedparser import parse
from HTMLParser import HTMLParser
from itertools import islice
from landing_page import db
from models import FeedItem
from time import mktime
import os
import re

def refresh_rss(url):
    ''' Deletes and re-fills the blog feed database with RSS entries '''
    feed = parse(url)
    if feed['bozo'] == 1:
        raise Exception, '%s is not a valid RSS stream!' % url

    items = []
    for item in islice(feed['items'], 5):
        feeditem = FeedItem(title=item.title,
                            description=truncate(strip_html(item.description, True)),
                            date=datetime.fromtimestamp(mktime(item.updated_parsed)),
                            url=item.link)
        items.append(feeditem)

    FeedItem.query.delete()
    db.session.add_all(items)
    db.session.commit()

def strip_html(string, remove_link_content=False):
    ''' Strip the string of HTML chars. We need to get rid of them, but we
        certainly don't want to eval them '''
    result = HTMLParser().unescape(re.sub('<[^<]+?>', '', string))
    if remove_link_content:
        return re.sub('Continue reading..', '', result)
    return result

def truncate(string, length=200, suffix='...'):
    ''' This function truncates the string to a given length without
        cutting the last word in half '''
    return string[:length].rsplit(' ', 1)[0]+suffix

def parse_media_mention(filename):
    ''' Get a MediaMention object out of a cfg file '''
    parser = SafeConfigParser()
    parser.read(filename)

    return MediaMention(
            title=parser.get('Mention', 'title'),
            quote=parser.get('Mention', 'quote'),
            url=parser.get('Mention', 'url'),
            author=parser.get('Mention', 'author'),
            priority=parser.get('Mention', 'priority'))

def get_media_mentions(path):
    ''' Load all the media mention files from a given path '''
    result = []
    for filename in [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.cfg')]:
        result.append(parse_media_mention(filename))
    # Returing a list sorted by priority reversed, hence the cmp function
    return sorted(result, cmp=lambda x,y: cmp(y.priority, x.priority))


class MediaMention:

    def __init__(self, title='', quote='', url='', author='', priority=''):
        self.title =  title
        self.quote =  quote
        self.url =    url
        self.author = author
        self.priority = priority
