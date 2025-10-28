from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.hr_login),
    path('job/', views.create_job),
    path('jobs/', views.get_all_jobs),
    path('job/<int:id>/', views.get_job_by_id),
    path('job/title/<str:title>/', views.get_job_by_title),
]
