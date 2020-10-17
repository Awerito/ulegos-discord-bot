from requests_html import HTMLSession


INIT_POS = 103

# Youtube search
#search = input("Youtube Search: ")
#search = str(search).replace(" ", "+").lower()
#search = "https://www.youtube.com/results?search_query=%s" % search
search = "https://www.youtube.com/results?search_query=wii+theme"
print(search)

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

print(titles)
