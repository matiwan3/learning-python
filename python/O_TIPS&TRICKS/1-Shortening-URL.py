import pyshorteners

def shorter_url(s: str):
    # initialize the shortener
    pys = pyshorteners.Shortener()
    # Using the tinyurl to shorten
    short_url = pys.tinyurl.shorten(s)
    return 'short url is', short_url