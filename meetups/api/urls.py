from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('meetups/', views.getMeetups),
    path('meetup/<int:id>', views.getMeetup),
    path('meetups/register', views.registrationView)
]