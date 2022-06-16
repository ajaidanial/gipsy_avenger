from django.urls import reverse_lazy


def template_common(request):
    """Common context for the templates."""

    return {
        "app_title": "Gipsy Avenger",
        "my_portfolio_url": "https://ajaidanial.wtf",
        "my_username": "ajaidanial",
        "navbar_links": [
            {"display": "Dashboard", "url": reverse_lazy("dashboard_page_view")},
            {"display": "Requests", "url": reverse_lazy("request_list_page_view")},
        ],
    }
