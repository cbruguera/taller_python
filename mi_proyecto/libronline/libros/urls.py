from django.conf.urls import patterns, url

from libros import views
from libros.views import GoogleBookInfoRedirectView, AutorDetailView, AutorListView
from libros.views import AutorCreateView, AutorUpdateView, AutorDeleteView


urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^$', AutorListView.as_view(), name='autor_index'),
    url(r'^autor/create/$', AutorCreateView.as_view(), name='autor_create'),
    url(r'^autor/edit/(?P<pk>\d+)/$', AutorUpdateView.as_view(), name='autor_edit'),
    url(r'^autor/delete/(?P<pk>\d+)/$', AutorDeleteView.as_view(), name='autor_delete'),
    #url(r'^libro/form/$', LibroFormView.as_view(), name='libro_form'),
    
    #url(r'^autor/save/$', AutorCreateView.as_view(), name='autor_save'),
    #url(r'^libro/save/$', None, name='libro_save'),
    
    url(r'^autor/(?P<pk>\d+)/$', AutorDetailView.as_view(), name='autor_detail'),
    url(r'search/(?P<pk>\d+)/$', GoogleBookInfoRedirectView.as_view()),
) 
