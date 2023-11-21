from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib import messages


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class AboutusPageView(generic.TemplateView):
    template_name = 'pages/aboutus.html'


def contact_us_page(request):
    messages.success(request, 'this is a success message')
    return render(request, "pages/contact_us.html")
