from django.shortcuts import render
from django.http import HttpResponse

from pictureserver.models import Picture


def index(request):

    pictures = Picture.objects.all()

    return render(
        request,
        'pictureserver/picture_list.html',
        {
            "pictures": pictures,
        }
    )
