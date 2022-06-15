from django.http import HttpResponse


def server_ping_view(request):
    """Just ping the server."""

    return HttpResponse("Pong!")
