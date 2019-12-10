from django.urls import path

from apps.core import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('quiz/', views.quiz, name='quiz'),
    path('results/', views.quiz, name="results"),
    
] 

urlpatterns += staticfiles_urlpatterns()
