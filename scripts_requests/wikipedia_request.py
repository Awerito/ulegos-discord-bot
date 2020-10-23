from urllib.request import urlopen
from re import findall
from requests_html import HTML


def wikipedia_request(search): 
    """This function parse and treats the results of a given search 

    Parameters
    ----------
    search: string
        parameter used to perform the search through Wikipedia

    Returns
    -------
    list[str]
        list of paragraphs with information about the article
        
    """
    
    # Wikipedia search
    search = str(search).replace(" ", "_").lower()
    search = "https://www.wikipedia.org/wiki/%s" % search
    
    # Wikipedia request
    session = urlopen(search)
    html_page = session.read()
    session.close()
    
    # Text cleaning
    # Text selection
    selection = 'p:not(.mw-empty-elt)'
    r = HTML(html=str(html_page))

    try:
        text = r.find(selection, first=True)
        return text.text
    except:
        return "No page was found"
