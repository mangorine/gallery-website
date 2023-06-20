
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

@login_required
def gallery(request, id=-1):
    context = {
        'id': id
    }
    return render(request, 'gallery.html', context)