from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'mediaanalytics'
urlpatterns = [
    # Views URLS
    path('', views.home, name='home'),
    path('article/', views.output, name='output'),
    path('timeline/', views.timeline, name='timeline'),
    path('nlp/', views.nlp, name='nlp'),
    path('about/', views.about, name='about'),
    path('article/<int:article_id>/', views.display, name='article'),
    
    # API URLS
    # POST requests
    path('api/articles/find/', views.getOvertime, name='articlesAPI'),
    path('api/articles/topwords/', views.getTopWords, name='getTopWords'),
    path('api/articles/similar/', views.getSimilarWords, name='getSimilarWords'),
    path('api/articles/notmatch/', views.getNotMatch, name='getNotMatch'),
    path('api/articles/similarity/', views.getSimilarity, name='getSimilarity'),
    path('api/articles/word/', views.getSpecificWord, name='getSpecificWord'),
    path('api/articles/xyz/', views.getAnalogies, name='getAnalogies'),
    # GET requests
    path('api/articles/find/<int:year1>/<int:year2>/<str:word>/', views.getOvertime, name='articlesAPI'),
    path('api/articles/similar/<int:yearID>/<str:wordToFind>/', views.getSimilarWords, name='getSimilarWords'),
    path('api/articles/topwords/<int:yearID>/', views.getTopWords, name='getTopWords'),
    path('api/articles/topwords/<int:yearID>/<int:breakID>/', views.getTopWords, name='getTopWords'),
    path('api/articles/similarity/<int:yearID>/<str:word1>/<str:word2>/', views.getSimilarity, name='getSimilarity'),
    path('api/articles/word/<int:yearID>/<str:word>/', views.getSpecificWord, name='getSpecificWord'),
    path('img/tsne/<int:yearID>/<str:words>/', views.getTSNE, name='getTSNE')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
