from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.urls import reverse

from profiles.models import Profile
User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = Profile

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]
    list_display = ('is_active', 'email', 'username', 'permalink', 'is_superuser', 'is_staff', 'date_joined')

    def permalink(self, obj):
        url = reverse('profiles:show', kwargs={'slug': obj.profile.slug})
        return format_html('<a href="{}">{}</a>'.format(url, '&#x1f517;'))
    permalink.allow_tags = True

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)