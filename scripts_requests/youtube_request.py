from urllib.request import urlopen
from re import findall


def youtube_request(search): 
    """Parse and treats the results of a given search 

    Parameters
    ----------
    search: string
        parameter used to perform the search through YouTube

    Returns
    -------
    str
        return the 'watch?v=' link segment
        
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
    if videos:
        return f'https://www.youtube.com/%s' % videos[0]
    return 'No video was found'
