import requests
import time
from bs4 import BeautifulSoup
import re


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

page = open("playlist", "r")
html = page.read()

soup = BeautifulSoup(html, "html.parser")


artists = soup.findAll("span", {"class": "TrackListRow__artists ellipsis-one-line"})
artist_names = []
for elem in artists:
    artist_elems = elem.find_all("a", {"class": "tracklist-row__artist-name-link"})
    total_artist_name = ""
    for name in artist_elems:
        total_artist_name += name.text.encode('ascii', 'ignore').decode('ascii') + ","
    
    artist_names.append(total_artist_name[:-1])

song_names = soup.findAll("div", {"class": "tracklist-name"})

for i in range(len(song_names)):
    artist = artist_names[i]
    song = re.findall(r'>(.+?)<', str(song_names[i]))[0]
    print '{} - {}'.format(artist, song)



