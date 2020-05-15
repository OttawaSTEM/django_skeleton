from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext as _
from authtools import views as authviews
# from braces import views as bracesviews
from django.conf import settings
from django.http import HttpResponseRedirect
import requests
from registration.backends.default.views import RegistrationView
from . import forms

# User = get_user_model()

# Use django-registeration, drop this
# class SignUpView(bracesviews.AnonymousRequiredMixin, bracesviews.FormValidMessageMixin, generic.CreateView):
#     form_class = forms.SignupForm
#     template_name = 'accounts/signup.html'
#     success_url = reverse_lazy('home')
#     form_valid_message = 'You're signed up!'
#
#     def form_valid(self, form):
#         redirect = super(SignUpView, self).form_valid(form)
#         username = form.cleaned_data['email']
#         password = form.cleaned_data['password1']
#         user = auth.authenticate(email=username, password=password)
#         auth.login(self.request, user)
#         return redirect


class SignUpView(RegistrationView):
    form_class = forms.SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Begin reCAPTCHA validation
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response}
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        # End reCAPTCHA validation  
        if result['success']:
            redirect = super(SignUpView, self).form_valid(form)
            return HttpResponseRedirect(reverse_lazy('register-complete')) 
        else:
            return HttpResponseRedirect('/')



# class LoginView(bracesviews.AnonymousRequiredMixin, authviews.LoginView):
class LoginView(authviews.LoginView):
    template_name = 'accounts/login.html'
    form_class = forms.LoginForm

    def form_valid(self, form):
        # Begin reCAPTCHA validation
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response}
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        # End reCAPTCHA validation
        if result['success']:
            redirect = super(LoginView, self).form_valid(form)
            remember_me = form.cleaned_data.get('remember_me')
            if remember_me is True:
                ONE_MONTH = 30*24*60*60
                expiry = getattr(settings, 'KEEP_LOGGED_DURATION', ONE_MONTH)
                self.request.session.set_expiry(expiry)
            # return redirect
            return HttpResponseRedirect(reverse_lazy('profiles:show_self'))
        else:
            return HttpResponseRedirect('/')


class LogoutView(authviews.LogoutView):
    url = reverse_lazy('home')


class PasswordChangeView(authviews.PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Your password was changed, hence you have been logged out. Please relogin'))
        return super(PasswordChangeView, self).form_valid(form)


class PasswordResetView(authviews.PasswordResetView):
    form_class = forms.PasswordResetForm
    template_name = 'accounts/password_reset.html'
    success_url = reverse_lazy('accounts:password-reset-done')
    subject_template_name = 'accounts/emails/password_reset_subject.txt'
    email_template_name = 'accounts/emails/password_reset_email.html'


class PasswordResetDoneView(authviews.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmView(authviews.PasswordResetConfirmAndLoginView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = forms.SetPasswordForm
    
    def get_success_url(self): # override this function if you want to use reverse
        return reverse_lazy('profiles:show_self')