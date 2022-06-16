from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView

from app.forms import AlterEC2RequestForm
from app.models import AlterEC2Log, AlterEC2Request


def server_ping_view(request):  # noqa
    """Just ping the server."""

    return HttpResponse("Pong!")


class DashboardPageView(TemplateView):
    """Landing page after authentication for the user."""

    template_name = "page_dashboard.html"

    def get_context_data(self, **kwargs):
        """Necessary context."""

        data = super().get_context_data(**kwargs)
        data.update(
            {
                "logs": AlterEC2Log.objects.order_by("-started_on").select_related(
                    "for_request"
                )
            }
        )
        return data


class AlterEC2RequestCreateView(CreateView):
    """View to create a scheduled request."""

    form_class = AlterEC2RequestForm
    template_name = "page_request_create.html"
    success_url = reverse_lazy("request_list_page_view")

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, "Successfully created the request!"
        )
        return super().get_success_url()


class AlterEC2RequestListView(ListView):
    """View to list all the scheduled requests."""

    queryset = AlterEC2Request.objects.order_by("-created").all()
    template_name = "page_request_list.html"


class AlterEC2RequestDeleteView(DeleteView):
    """View to delete a given scheduled request."""

    queryset = AlterEC2Request.objects.all()
    success_url = reverse_lazy("request_list_page_view")

    def post(self, request, *args, **kwargs):
        return self.delete(request=request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request=request, *args, **kwargs)

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, "Successfully deleted the request!"
        )
        return super().get_success_url()
