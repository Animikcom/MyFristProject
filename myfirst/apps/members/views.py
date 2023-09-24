from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Tblaccount, Tblbuilding


def index(request):
    # latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'members/list.html')
    pass

def detail(request, articel_id):
        pass
    # try:
    #      a= Article.objects.get (id = articel_id)
    # except:
    #      raise Http404 ("Статя не найдена")

    # latest_comments_list = a.comment_set.order_by('-id')[:5]

    # return render (request, 'articles/detail.html', {'article':a, 'latest_comments_list':latest_comments_list})