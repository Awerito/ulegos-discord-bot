from urllib.request import urlopen
from re import findall
from requests_html import HTML


def wikipedia_request(search): 
    """This function parse and treats the results of an given search 

    Parameters
    ----------
    search: string
        parameter used to perform the search through wikipedia

    Returns
    -------
    text: str
        text with information about the article
        
    """
    
    # Wikipedia search
    search = str(search).replace(" ", "_").lower()
    search = "https://www.wikipedia.org/wiki/%s" % search
    
    # Wikipedia request
    session = urlopen(search)
    page_html = session.read()
    session.close()
    
    # Text cleaning
    text = HTML(html=page_html)
    result = []
    for p in text.find('p'):
        result.append(p.text)

    return result
