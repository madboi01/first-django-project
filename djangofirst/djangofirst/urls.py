
from django.urls import path, include
from . import views

urlpatterns = [
    path('articles/',include('articles.urls')),
    path('about/',views.about),
    path('',views.homepage),
]
