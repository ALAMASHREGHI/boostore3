from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('aboutus/', views.AboutusPageView.as_view(), name='aboutus'),
    path('contactus/', views.contact_us_page, name='contactus'),
]
