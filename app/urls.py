from django.urls import path

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
]
