from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^id/(\w+)/$', views.viewBox),
    url(r'^updateBox/$', views.updateBox),
    url(r'^addItem/$', views.addItem),
    url(r'^label/(\w+)/$', views.genLabel),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^recent/$', views.RecentView.as_view(), name='recent'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<box_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
]
