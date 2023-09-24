from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('news/', include('news.urls')),
    path('grappelli/', include('grappelli.urls')),
    # path('members/',  include('members.urls')),
    path('admin/', admin.site.urls),

]
