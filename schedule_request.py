from urllib.request import urlopen

def schedule_request(search):
    """Description

    Parameters
    ----------
    search: str
        Number of semester you want to see

    Returns
    -------
    str:
        url to schedule you want to see
        
    """
    #http://horarios.ulagosvirtual.cl/2do%20semestre%202020_years_days_horizontal.html#table_160
    table = "table_" +str(157 + 3*search)
    search = str(search).lower()
    url_search = "http://horarios.ulagosvirtual.cl/2do%20semestre%202020_years_days_horizontal.html#" +str(table)

    # session = urlopen(url_search) 
    # html_page = session.read() 
    # session.close()
    
    

    return url_search

