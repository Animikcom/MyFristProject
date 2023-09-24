from django.contrib import admin
from django.db import connection
from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
# admin.site.register(Tblaccount)