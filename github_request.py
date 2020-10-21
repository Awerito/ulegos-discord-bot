from urllib.request import urlopen
from requests_html import HTML


def github_request(search): 
    """Parse and treats the results of a given search 

    Parameters
    ----------
    search: str
        parameter used to perform the search through GitHub

    Returns
    -------
    list[Elements]:
        return the 'user/repository' links segments
        
    """
    
    # GitHub search
    search = str(search).replace(" ", "+").lower()
    search = "https://github.com/search?q=%s" % search
    
    # GitHub request
    session = urlopen(search)
    html_page = session.read()
    session.close()

     
    # Repo selection
    selection = 'a.v-align-middle'
    r = HTML(html=str(html_page))

    try:
        repos = r.find(selection)
        return repos
    except:
        return "Not repo found"
