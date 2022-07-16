from django.urls import path
from student import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:pk>/', views.student_detail, name='student-detail'),
    path('student/<int:pk>/edit', views.student_edit_form, name='student-edit-form'),

]
