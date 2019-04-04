from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from . import views

urlpatterns = [path('i18n/', include('django.conf.urls.i18n'))]
urlpatterns += i18n_patterns(
    path('', views.HomePage.as_view(), name='home'),
    path('aboutus/', views.AboutPage.as_view(), name='about'),

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('registration/register/complete/', views.RegisterCompleteView, name='register-complete'),
    path('registration/activate/complete/', views.ActivationCompleteView, name='activate-complete'),
    path('registration/', include('registration.backends.default.urls')),
    path('webadmin/', admin.site.urls),
    path('users/', include('profiles.urls', namespace='profiles')),

    path('locations/', include('locations.urls', namespace='locations')),
    path('properties/', include('properties.urls', namespace='properties')),
    # path('properties-review/', include('properties_review.urls', namespace='properties-review'))
)

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
