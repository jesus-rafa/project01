from django.shortcuts import render
from django.views.generic import (
    TemplateView
)
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

#from django.shortcuts import render_to_response 

class HomePage(LoginRequiredMixin, TemplateView):
    #template_name = 'Reporte_Ingresos.html'
    template_name = 'panel.html'
    login_url = reverse_lazy('users_app:user-login')

class FechaMixim(object):

    def get_context_data(self, **kwargs):
        context = super(FechaMixim, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()

        return context


# def HomePage(LoginRequiredMixin, request):
#     login_url = reverse_lazy('users_app:user-login')

#     return render(request,"Reporte_Ingresos.html",{})
    #return render_to_response('Reporte_Ingresos.html', {'errors': errors}, context_instance=RequestContext(request))



    
class TemplatePruebaMixin(FechaMixim, TemplateView):
    template_name = "mixin.html"