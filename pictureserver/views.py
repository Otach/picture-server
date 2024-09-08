from django.http import HttpResponse


def index():
    return HttpResponse(b"Hello, World!")
