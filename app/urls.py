from django.urls import path

from . import views

urlpatterns = [
    path("server/ping/", views.server_ping_view),
    path("dashboard/", views.DashboardPageView.as_view(), name="dashboard_page_view"),
]
