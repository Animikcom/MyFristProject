from django.urls import path
from . import views

app_name= 'articles'

urlpatterns= [
    path('', views.index, name='index'),
    path('<int:articel_id>/', views.detail, name='detail'),
    path('<int:articel_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]   