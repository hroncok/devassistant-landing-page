import feedparser
import itertools

url = 'http://historje.tumblr.com/rss'

def generate_items(url):
    feed = feedparser.parse(url)

    for item in itertools.islice(feed["items"], 5):
        print item['title']
