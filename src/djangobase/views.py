# from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.translation import ugettext as _
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(generic.TemplateView):
    template_name = 'home.html'


class AboutPage(generic.TemplateView):
    template_name = 'aboutus.html'


def RegisterCompleteView(request):
    messages.success(request, _('Your account has been created, and activation email had been sent to your email address. Please check your email and activate your account.'))
    return render(request, 'home.html', {})


def ActivationCompleteView(request):
    messages.success(request, _('Your account is now activated.'))
    return render(request, 'home.html', {})
