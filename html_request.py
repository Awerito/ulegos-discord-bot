from requests_html import HTMLSession


# Youtube search
#search = input("Youtube Search: ")
#search = str(search).replace(" ", "+").lower()
#search = "https://www.youtube.com/results?search_query=%s" % search
search = "https://www.youtube.com/results?search_query=wii+theme+10+hrs"
print(search)

# Youtube request
session = HTMLSession()
r = session.get(search)
r.html.render()
print("Done!")

# Video selection
selection = "a#video-title"
videos = r.html.find(selection)
for video in videos:
    print(video)
