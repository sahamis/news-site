from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Article

# Create your views here.
def article_list(request):
    url="https://www.yomiuri.co.jp/"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    title=soup.select("h3")
    published_date=soup.select('time')
    link=soup.select('h3>a')
    articles=[]
    
    for i in range(1,10):
        Article.objects.update_or_create(pk=i+1,defaults={
            'title':title[i].text,
            'published_date':published_date[i].text,
            'url':link[i].get('href')}
        )
    
    articles=Article.objects.all()

    return render(request,'news/article_list.html',{'articles':articles})  