from django.contrib import admin
from django.urls import path, include
from .views import Home,Author, Book, Publication, SearchResult, Filter
urlpatterns = [
    path("",Home),
    path("Author",Author),
    path("Book",Book),
    path("Publication", Publication),
    path('Filter', Filter),
    path('SearchResult', SearchResult)

]