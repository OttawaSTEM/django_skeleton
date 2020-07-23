from django.urls import include, path, reverse_lazy
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from . import views, sitemaps
from allauth.account import views as allauth_views

sitemaps = {
    'static': sitemaps.StaticViewSitemap,
}

urlpatterns = [path('i18n/', include('django.conf.urls.i18n'))]
urlpatterns += i18n_patterns(
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('webadmin/', admin.site.urls),


    # path('accounts/login/', login_required(allauth_views.LoginView.as_view(success_url=reverse_lazy('home')))),
    path('accounts/', include('allauth.urls')),
    # path('accounts/profile', include('profiles.urls', namespace='profiles')),

    # path('accounts/', include('accounts.urls', namespace='accounts')),
    # path('registration/register/complete/', views.RegisterCompleteView, name='register-complete'),
    # path('registration/activate/complete/', views.ActivationCompleteView, name='activate-complete'),
    # path('registration/', include('registration.backends.default.urls')),
)

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
