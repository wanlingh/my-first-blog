from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/', views.post_list, name='post_list'),
    url(r'^post1/', views.post_list1, name='post_list1'),
    url(r'^post2/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    url(r'^post3/new/', views.post_new, name='post_new'),
    url(r'^post3/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]