import requests
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field, HTML

from allauth.account.forms import SignupForm, LoginForm, PasswordField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class AllauthSignupForm(SignupForm):
    password1 = PasswordField(label=_("Password"))
    password2 = PasswordField(label=_("Password (again)"))
    captcha = ReCaptchaField(label='', widget=ReCaptchaV2Checkbox)

    def signup(self, *args, **kwargs):
        return super(AllauthSignupForm, self).login(*args, **kwargs)

class AllauthLoginForm(LoginForm):
    captcha = ReCaptchaField(label='', widget=ReCaptchaV2Checkbox)

    def login(self, *args, **kwargs):
        return super(AllauthLoginForm, self).login(*args, **kwargs)


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('from_email'),
            Field('subject'),
            Field('message'),
            HTML('<div class="form-group my-4"><div class="g-recaptcha" data-sitekey="{}"></div></div>'.format(settings.RECAPTCHA_SITE_KEY)),
            Submit('sent', _('Send'), css_class='btn-primary submit_button'),
        )