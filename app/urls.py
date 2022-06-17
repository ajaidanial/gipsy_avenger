from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("server/ping/", views.server_ping_view),
    path("dashboard/", views.DashboardPageView.as_view(), name="dashboard_page_view"),
    # scheduled request
    path(
        "requests/",
        views.AlterEC2RequestListView.as_view(),
        name="request_list_page_view",
    ),
    path(
        "requests/create/",
        views.AlterEC2RequestCreateView.as_view(),
        name="request_create_page_view",
    ),
    path(
        "requests/<pk>/delete/",
        views.AlterEC2RequestDeleteView.as_view(),
        name="request_delete_page_view",
    ),
    # auth
    path(
        "auth/login/",
        views.AppLoginView.as_view(),
        name="login_page_view",
    ),
    path(
        "auth/logout/",
        views.AppLogoutView.as_view(),
        name="logout_page_view",
    ),
    path("", RedirectView.as_view(url=reverse_lazy("dashboard_page_view"))),
]
