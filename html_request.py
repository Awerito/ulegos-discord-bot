from requests_html import HTMLSession


INIT_POS = 103

def youtube_request(search): 
    """Description

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
    session = HTMLSession()
    r = session.get(search)
    r.html.render()
    
    # Video selection
    selection = "a#video-title"
    videos = r.html.find(selection)
    
    # Dictionary creation
    titles = {}
    for video in videos:
        string = str(video)
    
        first_pos = string[INIT_POS:].find("'") + INIT_POS
        second_pos = string[first_pos + 8:].find("'") + first_pos + 8
    
        title = string[INIT_POS:first_pos]
        link = string[first_pos + 8:second_pos]
    
        titles[title] = link
    
    return titles
