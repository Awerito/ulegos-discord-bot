from urllib.request import urlopen
from urllib.error import HTTPError
from requests_html import HTML
from imgkit import from_string

def _find_table(level):
    """I Hate UlagosVirtual"""

    if level == 1:
        return 163
    elif level == 2.1:
        return 169
    elif level == 2.2:
        return 166
    elif level == 3:
        return 172
    elif level == 4:
        return 175
    elif level == 6:
        return 178
    elif level == 7:
        return 181
    elif level == 8:
        return 184
    elif level == 10:
        return 187
    elif level == 12:
        return 193
    else:
        return -1


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

    table_id = _find_table(float(search))
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
        from_string(utf_8 + table_html.html, 'out.jpeg')
        print(table_html)
        return "Success"
    except:
        return "No table was found xd"
