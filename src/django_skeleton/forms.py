from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field, HTML


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