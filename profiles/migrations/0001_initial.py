# Generated by Django 5.0.7 on 2024-07-17 20:41

import django.core.validators
import django.db.models.deletion
import django_countries.fields
import profiles.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('avatar', models.ImageField(blank=True, null=True, storage=profiles.models.UploadStorage(), upload_to=profiles.models.upload_to, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'bmp', 'gif'])], verbose_name='Avatar Picture')),
                ('bio', models.CharField(blank=True, max_length=200, verbose_name='Short Bio')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email Verified')),
                ('phone_number', models.CharField(blank=True, max_length=20, verbose_name='Phone Number')),
                ('pobox', models.CharField(blank=True, max_length=20, verbose_name='P.O. Box')),
                ('apt_unit', models.CharField(blank=True, max_length=20, verbose_name='Apt/Unit')),
                ('street_num', models.CharField(blank=True, max_length=20, verbose_name='Street Number')),
                ('street_name', models.CharField(blank=True, max_length=50, verbose_name='Street Name')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='City/Town')),
                ('province', models.CharField(blank=True, choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Québec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')], db_index=True, max_length=2, verbose_name='Province')),
                ('country', django_countries.fields.CountryField(default='CA', max_length=2)),
                ('post_code', models.CharField(blank=True, max_length=7, verbose_name='Postal Code')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
