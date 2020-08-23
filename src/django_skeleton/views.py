import requests
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views import generic

from . import forms
from .utils import SendEmail

class HomePage(generic.TemplateView):
    template_name = 'home.html'

class AboutPage(generic.TemplateView):
    template_name = 'about.html'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        kwargs['contact_form'] = forms.ContactForm()
        return super(AboutPage, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        contact_form = forms.ContactForm(request.POST)
        if contact_form.is_valid():
            # Begin reCAPTCHA validation
            recaptcha_response = self.request.POST.get('g-recaptcha-response')
            data = {'secret': settings.RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response}
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            # End reCAPTCHA validation  
            if result['success']:
                SendEmail(from_email=contact_form.cleaned_data['from_email'], subject=contact_form.cleaned_data['subject'], body=contact_form.cleaned_data['message'])
                messages.success(request, _('Email sent!'))
            return HttpResponseRedirect('/about')
        else:
            messages.error(request, _('There was a problem with the form. Please check the details.'))
            return super(AboutPage, self).get(request, contact_form=contact_form)


def RegisterCompleteView(request):
    messages.success(request, _('Your account has been created, and activation email had been sent to your email address. Please check your email and activate your account.'))
    return render(request, 'home.html', {})

def ActivationCompleteView(request):
    messages.success(request, _('Your account is now activated.'))
    return render(request, 'home.html', {})
