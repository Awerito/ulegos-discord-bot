from urllib.request import urlopen
from re import findall


def youtube_request(search): 
    """This function parse and treats the results of an given search 

    Parameters
    ----------
    search: string
        parameter used to perform the search through youtube

    Returns
    -------
    dictionary
        values by title and link of the search. {str : str} 
        
    """
    
    # Youtube search
    search = str(search).replace(" ", "+").lower()
    search = "https://www.youtube.com/results?search_query=%s" % search
    
    # Youtube request
    session = urlopen(search)
    page_html = session.read()
    session.close()
    
    # Video selection
    videos = findall('watch\?v=\w*', str(page_html))
    return videos
