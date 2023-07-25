from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .settings import LOGIN_REDIRECT_URL, LOGIN_URL


def root_redirect(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse(LOGIN_REDIRECT_URL))
    else:
        return HttpResponseRedirect(reverse(LOGIN_URL))


def media(request, path):
    """
    When trying to access /media/path this function makes sures the user is authenticated.
    If it is the case then the media is served by the nginx server.
    Otherwise an http access error code is sent back.
    """
    access_granted = False
    user = request.user
    if user.is_authenticated:
        access_granted = True

    if access_granted:
        response = HttpResponse()
        # Content-type will be detected by nginx
        del response["Content-Type"]
        response["X-Accel-Redirect"] = "/protected/media/" + path
        return response
    else:
        return HttpResponseForbidden()


@login_required
def gallery(request, id=-1):
    context = {"id": id}
    return render(request, "gallery.html", context)


@login_required
def galleries(request):
    return render(request, "galleries.html")


def index(request):
    return render(request, "index.html")


def material(request):
    return render(request, "material.html")
