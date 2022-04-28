from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('searchhtml', views.add, name='add'),
    path('lists', views.lists, name = 'lists'),
    path('rec_lists', views.reclists, name = 'reclists')
]
urlpatterns += staticfiles_urlpatterns()