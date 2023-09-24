from django.urls import path
from . import views
from django.conf.urls.static import static

# app_name= 'news'

urlpatterns= [
    path('', views.news, name='news'),
    path('filter', views.filter, name='filter'),
    # path('<int:articel_id>/', views.detail, name='detail'),
    # path('<int:articel_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]   