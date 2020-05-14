from django.shortcuts import render

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, \
     PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class ClaseBase(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin):
    login_url='home:login'
    permission_required=""
    success_message = ""


class VistaAlta(ClaseBase,generic.CreateView):
    context_object_name='obj'
    success_message="Creado Satisfactoriamente"

    def form_valid(self, form):
        if form.instance.pk:
            form.instance.um = self.request.user.id
        else:
            form.instance.uc = self.request.user
        return super().form_valid(form)


class Home(LoginRequiredMixin,generic.TemplateView):
    template_name = 'home/home.html'




