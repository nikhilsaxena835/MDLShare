from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('searchhtml', views.add, name='add'),
    path('lists', views.lists, name = 'lists'),
    path('rec_lists', views.reclists, name = 'reclists'),
    path('movie_details', views.getdetails, name = 'getdetails'),
    #path('lists', TemplateView.as_view(template_name='lists.html'))
]
urlpatterns += staticfiles_urlpatterns()

