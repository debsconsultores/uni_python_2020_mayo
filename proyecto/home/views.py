from django.shortcuts import render

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, \
     PermissionRequiredMixin

class ClaseBase(LoginRequiredMixin,PermissionRequiredMixin):
    login_url='home:login'


class Home(ClaseBase,generic.TemplateView):
    template_name = 'home/home.html'



