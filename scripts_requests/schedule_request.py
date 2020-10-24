from urllib.request import urlopen
from urllib.error import HTTPError
from requests_html import HTML


def schedule_request(search):
    """Description

    Parameters
    ----------
    search: str
        Number of semester you want to see

    Returns
    -------
    HTML Object:
        table tag that contain schedule
        
    """

    URL = "http://horarios.ulagosvirtual.cl/2do%20semestre%202020_years_days_horizontal.html" 
    search = int(search)
    table_id = "table_" + str(157 + 3 * search)

    # Get HTML
    try:
        session = urlopen(URL) 
        html_page = session.read() 
        session.close()
    except HTTPError:
        return "Platea is possibly down"

    # Parse to html
    text = HTML(html=html_page)

    # Find table
    try:
        table_html = text.find('table#' + table_id)
        return table_html
    except:
        return "No table was found"
