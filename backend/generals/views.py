from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "generals/home.html"


class AboutPageView(TemplateView):
    template_name = "generals/about.html"
