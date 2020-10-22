from urllib.request import urlopen
from re import findall

def reddit_request(search):
    """Parse and treat the results of a given search

    Parameters
    ----------
    search: string
        parameter used to perform the search through Reddit

    Returns
    -------
    list[str]
        return the '/r/{search}/comments/' link segment
        
    """

    # Reddit search
    search = str(search).lower()
    search = "https://www.reddit.com/r/%s/" % search

    # Reddit requests
    session = urlopen(url_search) 
    html_page = session.read() 
    session.close()

    # Post selection
    posts = findall('/r/'+search+'/comments/\w*/\w*', str(html_page))
    return posts
