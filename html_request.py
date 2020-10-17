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

lists_results = []

# Video selection
selection = "a#video-title"
videos = r.html.find(selection)
for video in videos:
    print(video)

    aux_position_1 = video[104:].find("'")
    title = video[104:aux_position_1]
    aux_postition_2 = video[(aux_position_1+7):].find("'")
    link = video[(aux_position_1+7):aux_position_2] 

    #dictionary results
    dictionary_links{"title":title, "link":link}
    
    lists_results.append(dictionary_links)
