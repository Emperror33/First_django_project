from django.shortcuts import render
from django.http.response import HttpResponse, Http404,HttpResponsePermanentRedirect

# Create your views here.
articles= {
    'sports':'sports page',
    'finance':'finance page',
    'politics': 'politics page' 
}

def news_view(request,topic):
    try:
        result= articles[topic]
        return HttpResponse(articles[topic]) 
    except:
        raise Http404("404 GENERIC ERROR")

def num_page_view(request,num_page):
    topics_list = list(articles.keys())
    topic=topics_list[num_page]
    
    return HttpResponsePermanentRedirect(topic)