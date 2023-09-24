from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import pyodbc
from datetime import datetime, timedelta
# import pandas as pd



cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=WIN-IVTEF69OMJ5\ANIMIKSERVER;"
            "Database=Real EstateSQL;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()
# data = cursor.execute("SELECT TOP(100) * FROM tblOwners")

# meta = data.fetchall()

def news(request):
    try:
        data = cursor.execute("SELECT TOP(100) * FROM tblOwners")
        newss = data.fetchall()
        
        #  a= Article.objects.get (id = articel_id)
        #  b= Tblaccount.objects
    except:
         raise Http404 ("Статя не найдена")

    return render (request, 'news/news.html', {'newss':newss, },)

def filter(request):
    # if request.is_ajax():
        gfil = request.GET.get('select1', None)
        data = cursor.execute("SELECT TOP(100) * FROM tblOwners where FAMILY like=" + gfil )
        filtered = data.fetchall()
        filtered = 'dataaa'
        return JsonResponse({'text': 'HEllo-World'})
    # else:
        # return JsonResponse ({'text': "Это ложный запрос ajax"})

def ajax_get(request):
         # Определить, является ли текущий метод запроса ajax
    if request.is_ajax():
        city = request.GET.get('city')
        print(city)
        return JsonResponse ({'content': "Это запрос ajax"})
        # return render (request, 'index.html', {'content': 'Это запрос ajax'})
    else:
        return JsonResponse ({'content': "Это ложный запрос ajax"})
        # return render (request, 'index.html', {'content': 'Это ложный запрос ajax'})