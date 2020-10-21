from urllib.request import urlopen
from re import findall
from requests_html import HTML


def github_request(search='linux'): 
    """Parse and treats the results of a given search 

    Parameters
    ----------
    search: str
        parameter used to perform the search through GitHub
        'linux' by default

    Returns
    -------
    list[str]
        return the '/user/repository' link segment
        
    """
    
    # GitHub search
    # https://github.com/search?q=linux
    search = str(search).replace(" ", "+").lower()
    search = "https://github.com/search?q=%s" % search
    
    # GitHub request
    session = urlopen(search)
    html_page = session.read()
    session.close()

    # regex_1 = """"github.com\/\w*\/\w*\"\}"""
    # regex_2 = """"github.com\/\w*\/\w*\-\w*\"\}"""

    regex_3 = '\"\/\w*\/\w*\"'
    regex_4 = '\"\/\w*\/\w*-\w*\"'
    
    # Repo selection
    repos = findall(regex_3, str(html_page))

    return repos
