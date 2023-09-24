import datetime
from django.db import models
from django.utils import timezone



class Article(models.Model):
     article_title = models.CharField('Название статьи', max_length=200)
     articl_text = models.TextField('Текст статьи')
     pub_date = models.DateTimeField ('Дата публикации')

     def __str__(self):
         return self.article_title

     def was_published_recently(self):
         return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

     class Meta:
         verbose_name = 'Статя'
         verbose_name_plural = 'Статьи'
    


class Comment(models.Model):
     article = models.ForeignKey(Article, on_delete=models.CASCADE)
     author_name = models.CharField ('имя автора', max_length= 50)
     comment_text = models.CharField ('текст комментария', max_length=200)

     def __str__(self):
         return self.author_name
    
     class Meta:
         verbose_name = 'Комментарий'
         verbose_name_plural = 'Комментарии'
         
# class Tblaccount(models.Model):
#     account = models.CharField('имя family',max_length=20, blank=True, null=True) 
#     family = models.CharField('имя family',max_length=20, blank=True, null=True) 
#     name = models.CharField('имя name',max_length=20, blank=True, null=True) 
#     second = models.CharField('имя second',max_length=20, blank=True, null=True)  
#     pasport = models.CharField('имя pasport',max_length=120, blank=True, null=True) 
#     born = models.DateTimeField('имя born',blank=True, null=True)  
#     username = models.CharField('имя username',max_length=20, blank=True, null=True) 
#     datetime = models.DateTimeField('имя datetime',blank=True, null=True) 
#     hostname = models.CharField('имя hostname',max_length=20, blank=True, null=True) 
#     clientname = models.CharField('имя clientname',max_length=128, blank=True, null=True)
#     def __str__(self):
#          return self.username