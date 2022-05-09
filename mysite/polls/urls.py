from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('searchhtml', views.add, name='add'),
    path('lists', views.lists, name = 'lists'),
    path('rec_lists', views.reclists, name = 'reclists'),
    path('movie_details', views.getdetails, name = 'getdetails'),
    path('login', views.login, name = 'login'),
    path('profile', views.profile_page, name = 'profile_page'),
    path('search', views.search, name = 'search'),
    path('about', views.about, name = 'about'),
    #path('lists', TemplateView.as_view(template_name='lists.html'))
]
urlpatterns += staticfiles_urlpatterns()



