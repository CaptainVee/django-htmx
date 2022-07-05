from django.urls import path
from .views import article_detail_view, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('article_detail/<int:id>', article_detail_view, name='details'),

]
