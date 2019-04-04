from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field, HTML

from . import models

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(Field('name')
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [# 'picture', 
            'phone_number', 'pobox', 'apt_unit', 'street_num', 'city', 'province', 'country', 'post_code'
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            # Add Picture
            Div(Div(HTML(_('Add Avatar Picture')), style='font-size: 1.3em; font-weight: bold; margin-bottom: 10px;'),
                HTML('<p id="added_avatar_image" style="display: inline;"></p>'),
                HTML('<p style="display: inline;"><a id="avatar_image_add" class="thumbnail-image" href="#"><img src="{}site/img/add.png" alt="Add Image"></a></p>'.format(settings.STATIC_URL)),
                Div(HTML('<input id="avatar_input" type="file" accept="image/gif, image/jpeg, image/png" value=""/>'), style='width: 0px; height: 0px; overflow: hidden')),

            # Field('picture'),
            Field('phone_number'),
            Field('pobox'),
            Field('apt_unit'),
            Field('street_num'),
            Field('street_name'),
            Field('city'),
            Field('province'),
            Field('post_code'),
            Field('country'),
            Submit('update', _('Update'), css_class='btn-primary'),
        )
