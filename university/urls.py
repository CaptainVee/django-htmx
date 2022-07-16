from django.urls import path
from university import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('modules/', views.modules, name='modules')
]
