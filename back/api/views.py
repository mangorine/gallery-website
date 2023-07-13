from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.parsers import FileUploadParser

from django.template.defaultfilters import slugify

from api.models import (
    Student, Gallery, File, Reaction, Material, Year
)

from api.serializers import (
    GallerySerializer, FileSerializer, PromoSerializer, YearSerializer
)

import galerie.loader as loader
import galerie.settings as settings
import os

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/api/galleries",
            "method": "GET",
            "description": "Return all galleries that a user can see",
        },
        {
            "Endpoint": "/api/galleries/create",
            "method": "POST",
            "description": "Create a new gallery",
            "Format of the request:": {
                "name": "name of the gallery",
                "description": "gallery's description",
                "date":"creation date",
                "visibility": "gallery's visibility",
                "type":"photo or video?",
                "year": "creation date's year",
            },
        },
        {
            "Endpoint": "/api/gallery/pics",
            "method": "GET",
            "description": "Return all pics from a gallery",
            "Format of the request:": {
                "id": "gallery_id",
            },
        },
        {
            "Endpoint": "/api/year/create",
            "method": "POST",
            "description": "Create a new year",
            "Format of the request:": {
                "name": "name of the year (eg. 2022-2023)",
            },
        },
        {
            "Endpoint": "/api/promo/create",
            "method": "POST",
            "description": "Create a new promotion",
            "Format of the request:": {
                "name": "name of the promo (eg. 026)",
                "year": "year object corresponding to first year of this promo"
            },
        }
    ]

    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_galleries(request):
    galleries = Gallery.objects.filter(visibility=Gallery.Visibility.PUBLIC).order_by('-date')
    serializer = GallerySerializer(galleries, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_gallery(request):
    print(request.data['id'])
    gallery = Gallery.objects.filter(id=request.data['id'])
    if(gallery.count() == 0):
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GallerySerializer(gallery[0])
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_pics(request):
    files = File.objects.filter(gallery = request.data['id'])
    if(files.count() == 0):
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FileSerializer(files, many=True)
    return Response(data=serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_gallery(request):
    if('year' not in request.data):
        request.data['year'] = Year.objects.last().pk
    request.data['slug'] = slugify(request.data['name'])
    serializer = GallerySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    os.mkdir(str(settings.BASE_DIR) + '/media/' + request.data['slug'])
    os.mkdir(str(settings.BASE_DIR) + '/media/' + request.data['slug'] + '/uploads')
    os.mkdir(str(settings.BASE_DIR) + '/media/' + request.data['slug'] + '/thumbnails')
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_year(request):
    serializer = YearSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_promo(request):
    serializer = PromoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def load_folder_into_gallery(request):
    gal = Gallery.objects.get(id=request.data['id'])
    loader.load_folder_into_gallery(request.data['folder'], gal)
    return Response(GallerySerializer(gal).data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def generate_thumbnails(request):
    loader.generate_thumbnails(request.data['folder'])
    return Response(status=200)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def delete_gallery(request):
    gal = Gallery.objects.get(name=request.data['name'])
    gal.delete()
    #TODO DELETE FOLDER
    return Response(GallerySerializer(gal).data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def delete_pic(request):
    gallery =  Gallery.objects.get(name=request.data['name'])
    file = File.objects.get(gallery=gallery, link=request.data['link'])
    file.delete()
    #TODO DELETE FILE CONCERNED
    return Response(FileSerializer(file).data)

class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    permission_classes = [IsAdminUser]
    
    def put(self, request, filename, format='jpg'):
        file_obj = request.data['file']
        file = open(str(settings.BASE_DIR) + "/galerie/media/"+ filename)
        for chunk in file_obj.chunks():
            file.write(chunk)
        file.close()
        return Response(status=204)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def import_users(request):
    read_users(str(settings.BASE_DIR) + '/api/users.sql')
    return Response(status=200)

def read_users(file):
            f = open(file, encoding='utf8')
            f.readline()
            i = 0
            for l in f:
                if i < 10:
                    args = l.replace('(', '').replace(')', '').split(',')
                    uid = int(args[0])
                    firstname = args[2].replace("'", "").replace(" ", "")
                    lastname = args[3].replace("'", "").replace(" ", "")
                    year = args[6].replace("'", "")
                    username = args[8].replace("'", "").replace(" ", "")
                    mail = args[9].replace("'", "")
                    join_date = args[12].replace("'", "").split(" ")[1]
                    print(uid, firstname, lastname, year, username, mail, join_date)

                    user = User.objects.create_user(username=username, email=mail, password="e")
                    user.first_name = firstname
                    user.last_name = lastname
                    user.date_joined = join_date
                    user.save()
                    i += 1
                else:
                    break