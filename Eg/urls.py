# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('about',views.about,name='about'),
    path('reg', views.registration_view, name='reg'),
    path('next/<str:pk>/',views.nextpage,name='next'),
    path('last/<str:pk>/',views.submit,name='last'),
    path('success/<str:pk>/',views.success,name='success'),
    path('favicon.ico', views.favicon_view, name='favicon'),
]


