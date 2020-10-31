from urllib.request import urlopen
from urllib.error import HTTPError
from requests_html import HTML
from imgkit import from_string


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

    table_id = 157 + 3 * int(search)
    url = "http://horarios.ulagosvirtual.cl/2do%20semestre%202020_years_days_horizontal.html" 
    table_id = "#table_" + str(table_id)
    url += table_id

    # Get HTML
    try:
        session = urlopen(url) 
        html_page = session.read() 
        session.close()
    except HTTPError:
        return "Platea is possibly down"

    # Parse to html
    text = HTML(html=html_page)

    # Find table
    try:
        table_html = text.find(table_id, first=True)
        utf_8 = '<meta charset="utf-8">\n'
        render = from_string(utf_8 + table_html.html, 'out.jpeg')
        return "Success"
    except:
        return "No table was found"
