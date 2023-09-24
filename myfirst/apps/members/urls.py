from django.urls import path
from . import views

app_name= 'members'

urlpatterns= [
    path('', views.index, name='index'),
    path('<int:member_id>/', views.detail, name='detail'),
    path('<int:member_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]   