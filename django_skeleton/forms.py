from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, HTML

from allauth.account.forms import SignupForm, LoginForm, PasswordField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class AllauthSignupForm(SignupForm):
    password1 = PasswordField(label=_("Password"))
    password2 = PasswordField(label=_("Password (again)"))
    captcha = ReCaptchaField(label='', widget=ReCaptchaV3)

    def signup(self, *args, **kwargs):
        return super(AllauthSignupForm, self).login(*args, **kwargs)


class AllauthSigninForm(LoginForm):
    captcha = ReCaptchaField(label='', widget=ReCaptchaV3)

    def login(self, *args, **kwargs):
        return super(AllauthSigninForm, self).login(*args, **kwargs)


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
            HTML(
                '<input type="hidden" id="g-recaptcha-response" name="g-recaptcha-response">'),
            Submit('sent', _('Send'), css_class='btn-primary submit_button'),
        )
