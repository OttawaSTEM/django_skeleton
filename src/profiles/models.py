import os, uuid
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from rentbnb.constants import DATA


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here with default values,
    # CharFiled and TextFiled discouraged to use null=True in Django, avoid two possible values for “no data”: null and the empty string
    # python manage.py makemigrations profiles --name AddProfileModels
    picture = models.ImageField(_('Profile Picture'), max_length=200, blank=True, null=True)
    bio = models.CharField(_('Short Bio'), max_length=200, blank=True)
    email_verified = models.BooleanField(_('Email Verified'), default=False)
    phone_number = models.CharField(_('Phone Number'), max_length=20, blank=True)
    pobox = models.CharField(_('P.O. Box'), max_length=20, blank=True)
    apt_unit = models.CharField(_('Apt/Unit'), max_length=20, blank=True)
    street_num = models.CharField(_('Street Number'), max_length=20, blank=True)
    street_name = models.CharField(_('Street Name'), max_length=50, blank=True)
    city = models.CharField(_('City/Town'), max_length=30, blank=True)
    province = models.CharField(_('Province'), max_length=2, blank=True, db_index=True, choices=DATA.PROVINCE)
    country = CountryField(default='CA')
    post_code = models.CharField(_('Postal Code'), max_length=7, blank=True)


    class Meta:
        abstract = True


class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
