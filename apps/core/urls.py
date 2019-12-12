from django.urls import path

from apps.core import views



urlpatterns = [
    path('', views.home, name='home'),
    path('locate/', views.about, name='locate'),
    path('quiz/', views.quiz, name='quiz'),
    path('results/', views.quiz, name="results"),
    
] 


