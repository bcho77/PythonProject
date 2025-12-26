from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path("tutorial/<slug:topic>/", views.tutorial_detail, name="tutorial-detail"),

#
]



