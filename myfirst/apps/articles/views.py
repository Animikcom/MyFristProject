
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Article, Comment


def index(request):
     latest_articles_list = Article.objects.order_by('-pub_date')[:5]
     Tblaccount = Tblaccount.objects.order_by('account')
     return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list, 'Tblaccount': Tblaccount}, )


def detail(request, articel_id):
    try:
         a= Article.objects.get (id = articel_id)
         b= Tblaccount.objects
    except:
         raise Http404 ("Статя не найдена")

    latest_comments_list = a.comment_set.order_by('-id')[:5]

    return render (request, 'articles/detail.html', {'article':a, 'latest_comments_list':latest_comments_list, 'Tblaccount': Tblaccount}, )

def leave_comment(request, articel_id):
        try:
         a = Article.objects.get (id = articel_id)
        except:
             raise Http404 ("Статя не найдена")
        a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
        return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
