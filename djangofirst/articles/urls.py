from django.urls import path
from .import views

urlpatterns = [
    path('',views.articles_list),
    path('<slug:slug>/',views.article_detail),
]
