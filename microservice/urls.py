from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #path("", views.urlShort, name="home"),
    path("u/<str:short>", views.urlRedirect, name="redirect"),
    path("",views.short_url_data)
]