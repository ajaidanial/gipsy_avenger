from django.http import HttpResponse
from django.views.generic import TemplateView


def server_ping_view(request):
    """Just ping the server."""

    return HttpResponse("Pong!")


class DashboardPageView(TemplateView):
    """Landing page after authentication for the user."""

    template_name = "page_dashboard.html"
