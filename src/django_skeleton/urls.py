from django.urls import include, path, reverse_lazy
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from . import views, sitemaps
from allauth.account import views as allauth_views
from websocket.urls import websocket

sitemaps = {
    'static': sitemaps.StaticViewSitemap,
}

# urlpatterns = [         # Switch to single language (English)
urlpatterns = [path('i18n/', include('django.conf.urls.i18n'))]
urlpatterns += i18n_patterns(
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),          # Remove Django admin login for security reason

    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', include('profiles.urls', namespace='profiles')),

    path('chat/', include('chat.urls')),
    websocket('ws/', views.websocket_view),
)

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
