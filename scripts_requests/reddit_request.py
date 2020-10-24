from urllib.request import urlopen
from urllib.error import HTTPError
from re import findall
from requests_html import HTML

def reddit_request(search):
    """Parse and treat the results of a given search

    Parameters
    ----------
    search: string
        parameter used to perform the search through Reddit

    Returns
    -------
    list[str]
        return the '/{search}/comments/' link segment
        
    """

    # Reddit search
    search = str(search).lower().replace(' ', '_')
    search = "https://www.reddit.com/%s/" % search

    # Reddit requests
    try:
        session = urlopen(search)
        html_page = session.read()
        session.close()
    except HTTPError:
        return "Go to talk with your Boss of Career"

    # Post selection
    posts = findall('/' + search + '/comments/\w*/\w*', str(html_page))

    pass


if __name__=="__main__":

    print(reddit_request('r/gaming'))
