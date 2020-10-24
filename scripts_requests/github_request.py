from urllib.request import urlopen
from urllib.error import HTTPError
from requests_html import HTML


def github_request(search): 
    """Parse and treats the results of a given search 

    Parameters
    ----------
    search: str
        parameter used to perform the search through GitHub

    Returns
    -------
    list[str]:
        return the 'user/repository' links segments
        
    """

    # GitHub search
    search = str(search).replace(" ", "+").lower()
    search = "https://github.com/search?q=%s" % search

    # GitHub request
    try:
        session = urlopen(search)
        html_page = session.read()
        session.close()
    except HTTPError:
        return "No repo was found"


    # Repo selection
    selection = 'a.v-align-middle'
    r = HTML(html=str(html_page))

    try:
        repo = r.find(selection, first=True)
        return 'https://www.github.com/' + repo.text
    except:
        return "No repo found"
