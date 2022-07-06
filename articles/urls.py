from django.urls import path
from .views import article_detail_view, home_view, article_search_view, article_create_view


urlpatterns = [
    path('', home_view, name='home'),
    path('article/', article_search_view, name='search'),
    path('article/create', article_create_view, name='create'),
    path('article_detail/<int:id>', article_detail_view, name='details'),

]
