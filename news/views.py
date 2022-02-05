# from django.shortcuts import render

# # Create your views here.
import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup =BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from Hindustan times

ht_r = requests.get("https://www.hindustantimes.com/india-news/")
#ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_soup = BeautifulSoup(ht_r.content,"html.parser")
ht_headings = ht_soup.findAll("h3", {"class": "hgd3"})
ht_headings = ht_headings[0:-13]
#ht_headings = ht_soup.find_all('h3')

ht_headings = ht_headings[0:-13] # removing footers
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(request):
    return render(request, 'index.html', {'toi_news':toi_news, 'ht_news': ht_news})
