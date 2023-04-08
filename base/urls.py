from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post/', views.post),
    path('post/<int:id>', views.post)
]