from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.ResumeFormView.as_view()),
    path('get_all_resumes', views.GetAllResumesView.as_view()),
]

