from urllib.request import urlopen
from re import findall

def reddit_request(search):
    """Description

    Parameters
    ----------
    param1 : type
        Description

    Returns
    -------
    type
        Description
        
    """
    #Reddit Request on ¿r?
    search = str(search).lower()
    url_search = "https://www.reddit.com/r/%s/" % search

    session = urlopen(url_search) 
    html_page = session.read() 
    session.close()

    posts = findall('/r/'+search+'/comments/\w*', str(html_page))

    return posts
