from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add/$', views.add, name="add"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^add/add_book/$', views.add_book, name="add_book"),
    url(r'^(?P<id>\d+)$', views.show_book, name="show_book"),
    url(r'^(?P<id>\d+)/add_review/$', views.add_review, name="add_review"),
    url(r'^(?P<id>\d+)/destroy/(?P<review_id>\d+)$', views.destroy, name="destroy"),
    url(r'^users/(?P<id>\d+)$', views.show_user, name="show_user"),
    url(r'^add/add_author/$', views.add_author, name="add_author"),
]
