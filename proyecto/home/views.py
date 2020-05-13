from django.shortcuts import render

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, \
     PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class ClaseBase(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin):
    login_url='home:login'
    permission_required=""
    success_message = ""


class Home(ClaseBase,generic.TemplateView):
    template_name = 'home/home.html'



