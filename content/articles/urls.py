from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listing_article, name='listing_article'),
    path('add/', views.add_article, name='add_article'),
    path('vote/', views.vote, name='vote'),
]
