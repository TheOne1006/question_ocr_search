
from haystack.views import SearchView
from django.urls import path, include
from haystack.views import SearchView
from haystack.query import SearchQuerySet
from .views import eSearch, IndexView

urlpatterns = [
    path('search', eSearch),
    path('index', IndexView.as_view())
]