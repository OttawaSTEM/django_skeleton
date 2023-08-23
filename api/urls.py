from django.urls import include, path

from . import views

app_name = "api"
urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/google/", views.GoogleSignin.as_view(), name="google_login"),  # Google social account
    path("auth/registration/", include("dj_rest_auth.registration.urls")),  # Local registration
    path("users/", views.UserView.as_view()),
    path("groups/", views.GroupView.as_view()),
]
