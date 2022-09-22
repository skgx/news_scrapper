
import requests
from django.shortcuts import render
from bs4 import BeautifulSoup


toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup =BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13]

toi_news = []
i=1
for th in toi_headings:
    if i>2:
      toi_news.append(th.text)
    i=i+1


def index(request):
    return render(request, 'index.html', {'toi_news':toi_news})
