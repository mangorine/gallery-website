from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u : u.is_superuser)
def index_view(request):
    return render(request, 'gestionindex.html')

@user_passes_test(lambda u : u.is_superuser)
def gallery_view(request, id=-1):
    context = {
        'id': id
    }
    return render(request, 'gestiongallery.html', context)
