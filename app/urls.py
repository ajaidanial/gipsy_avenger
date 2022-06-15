from django.urls import path

from . import views

urlpatterns = [path("server/ping/", views.server_ping_view)]
