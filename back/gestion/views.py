from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import FileSystemStorage
from galerie.loader import  load_zip_into_gallery
from api.models import Gallery

@user_passes_test(lambda u : u.is_superuser)
def index_view(request):
    return render(request, 'gestionindex.html')

@user_passes_test(lambda u : u.is_superuser)
def gallery_view(request, id=-1):
    context = {
        'id': id
    }
    if request.method == 'POST' and request.FILES['zipfile'] :
        file = request.FILES['zipfile']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)

        gal = Gallery.objects.get(id=id)
        print(uploaded_file_url.split('/')[2])
        load_zip_into_gallery(uploaded_file_url.split('/')[2], gal)
        fs.delete(filename)
    return render(request, 'gestiongallery.html', context)
