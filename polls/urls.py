'''
Created on 4 Oct 2015

@author: khairulimam
'''

from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.IndexView.as_view(), name='index'),
               url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
               url(r'^(?P<pk>[0-9]+)/result/$', views.ResultsView.as_view(), name="result"),
               url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"), ]
