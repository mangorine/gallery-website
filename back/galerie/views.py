from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .settings import LOGIN_REDIRECT_URL, LOGIN_URL

from api.models import Gallery

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
    user = request.user
    dirs = path.split("/")
    gallery =  Gallery.objects.filter(slug=dirs[0])
    if gallery.count() == 0:
        print("gallery not found")
        return HttpResponseForbidden()
    else:
        access_granted = gallery.first().can_user_access(user)
    
    if access_granted:
        response = HttpResponse()
        # Content-type will be detected by nginx
        del response["Content-Type"]
        response["X-Accel-Redirect"] = "/protected/media/" + path
        return response
    else:
        return HttpResponseForbidden()


def gallery(request, slug=""):
    context = {"slug": slug}
    return render(request, "gallery.html", context)


def galleries(request):
    return render(request, "galleries.html")


def index(request):
    return render(request, "index.html")


def material(request):
    return render(request, "material.html")
