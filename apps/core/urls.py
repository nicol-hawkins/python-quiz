from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('quiz/', views.quiz, name='quiz'),
    path('results/', views.results, name="results"),
    
]
