from django.http import HttpResponse
from django.views.generic import TemplateView

from app.models import AlterEC2Log


def server_ping_view(request):  # noqa
    """Just ping the server."""

    return HttpResponse("Pong!")


class DashboardPageView(TemplateView):
    """Landing page after authentication for the user."""

    template_name = "page_dashboard.html"

    def get_context_data(self, **kwargs):
        """Necessary context."""

        data = super().get_context_data(**kwargs)
        data.update({"logs": AlterEC2Log.objects.select_related("for_request")})
        return data
