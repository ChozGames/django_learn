from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    # path('article/<int:id_article>', views.view_article), 
    # path('articles/<str:tag>', views.list_articles_by_tag), 
    path('articles/<int:year>/<int:month>', views.list_articles), 
    path('google', views.google), 
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('article/<int:id>', views.lire, name='lire'),
     path('article/<slug:slug>', views.lire, name='lire'),
]