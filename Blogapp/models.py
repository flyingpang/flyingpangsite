#coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, User


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name


# class Classification(models.Model):
#     name = models.CharField(max_length=20)
#
#     def __unicode__(self):
#         return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name


class Article(models.Model):
    TYPE_CHOICES = (
        ('Django', _(u'Django')),
        ('Linux', _(u'Linux')),
        ('Python', _(u'Python')),
        ('CSS', _(u'CSS')),
        ('Other', _(u'Other'))
    )
    caption = models.CharField(max_length=30)
    subcaption = models.CharField(max_length=60, blank=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, related_name='articles', related_query_name='article')
    # classification = models.ForeignKey(Classification)
    classification = models.CharField(_(u'type'), max_length=20, choices=TYPE_CHOICES, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()































