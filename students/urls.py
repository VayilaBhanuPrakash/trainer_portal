from django.urls import path

from . import views

urlpatterns = [
     path('create/', views.create_student_view, name='student_create'),
     path('list/', views.student_list_view, name='student_list'),
     path('update/<str:student_id>/', views.update_student_view, name='student_update'),
     path('delete/<str:student_id>/', views.delete_student_view, name='student_delete'),
]