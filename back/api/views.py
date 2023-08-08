from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.parsers import FileUploadParser

from django.template.defaultfilters import slugify

from api.models import Gallery, File, Year

from api.serializers import (
    GallerySerializer,
    FileSerializer,
    PromoSerializer,
    YearSerializer,
)

import galerie.loader as loader
import galerie.settings as settings
import os


@api_view(["GET"])
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
                "date": "creation date",
                "visibility": "gallery's visibility",
                "type": "photo or video?",
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
                "year": "year object corresponding to first year of this promo",
            },
        },
    ]

    return Response(routes)

@api_view(["GET"])
def get_galleries(request):
    if(not request.user.is_authenticated):
        galleries = Gallery.objects.filter(visibility=Gallery.Visibility.PUBLIC).order_by(
        "-date"
    )
    elif(request.user.is_staff or request.user.is_superuser):
        galleries = Gallery.objects.all().order_by("-date")
    else:
        galleries = Gallery.objects.filter(Q(visibility=Gallery.Visibility.SCHOOL) | Q(visibility=Gallery.Visibility.PUBLIC)).order_by(
        "-date"
    )
    serializer = GallerySerializer(galleries, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def get_gallery(request):
    gallery = Gallery.objects.filter(slug=request.data["slug"])
    if gallery.count() == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #check if request user is allowed to see this gallery
    if(not request.user.is_authenticated and (not gallery[0].visibility == Gallery.Visibility.PUBLIC)):
        return Response({"status": "error", "message":"Vous n'êtes pas autorisé à voir cette galerie."}, status=403)
    elif(not request.user.is_staff and not request.user.is_superuser and gallery[0].visibility is Gallery.Visibility.PRIVATE):
        return Response({"status": "error", "message":"Vous n'êtes pas autorisé à voir cette galerie."}, status=403)
    else: 
        serializer = GallerySerializer(gallery[0])
        return Response(serializer.data)


@api_view(["POST"])
def get_pics(request):
    gallery = Gallery.objects.filter(slug=request.data["slug"])
    if gallery.count() == 0:
        return Response({"status": "error", "message":"Cette galerie n'existe pas."}, status=404)
    #check if request user is allowed to see this gallery
    if(not request.user.is_authenticated and (not gallery[0].visibility == Gallery.Visibility.PUBLIC)):
        return Response({"status": "error", "message":"Vous n'êtes pas autorisé à voir cette galerie."}, status=403)
    elif(not request.user.is_staff and not request.user.is_superuser and gallery[0].visibility is Gallery.Visibility.PRIVATE):
        return Response({"status": "error", "message":"Vous n'êtes pas autorisé à voir cette galerie."}, status=403)
    else: 
        files = File.objects.filter(gallery=gallery.first())
        serializer = FileSerializer(files, many=True)
        return Response(data=serializer.data)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_gallery(request):
    if "year" not in request.data:
        request.data["year"] = Year.objects.last().pk
    request.data["slug"] = slugify(request.data["name"])
    if(request.data['name'] == ''):
        return Response({"status":"error", "message": "Le nom de la galerie ne peut pas être vide."}, status=400)
    if(Gallery.objects.filter(slug=request.data["slug"]).exists()):
        return Response({"status":"error", "message": "Une galerie avec ce nom existe déjà."}, status=400)
    serializer = GallerySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    try:
        os.mkdir(str(settings.BASE_DIR) + "/media/" + request.data["slug"])
        os.mkdir(str(settings.BASE_DIR) + "/media/" + request.data["slug"] + "/uploads")
        os.mkdir(str(settings.BASE_DIR) + "/media/" + request.data["slug"] + "/thumbnails")
    except:
        return Response({"status":"error", "message": "Impossible de créer les dossiers galeries."}, status=400)

    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_year(request):
    serializer = YearSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_promo(request):
    serializer = PromoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes(
    (
        IsAuthenticated,
        IsAdminUser,
    )
)
def load_folder_into_gallery(request):
    gal = Gallery.objects.get(slug=request.data["slug"])
    loader.load_folder_into_gallery(request.data["folder"], gal)
    return Response(GallerySerializer(gal).data)


@api_view(["POST"])
@permission_classes(
    (
        IsAuthenticated,
        IsAdminUser,
    )
)
def generate_thumbnails(request):
    loader.generate_thumbnails(request.data["folder"])
    return Response(status=200)

@api_view(["POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def change_visibility(request):
    gallery = Gallery.objects.filter(slug=request.data["slug"])
    if gallery.count() == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)
    gallery = gallery[0]
    gallery.visibility = request.data["visibility"]
    gallery.save()
    return Response(GallerySerializer(gallery).data)

@api_view(["POST"])
@permission_classes([IsAdminUser])
def delete_gallery(request):
    gal = Gallery.objects.get(name=request.data["name"])
    gal.delete()
    # TODO DELETE FOLDER
    return Response(GallerySerializer(gal).data)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def delete_pic(request):
    gallery = Gallery.objects.get(name=request.data["name"])
    file = File.objects.get(
        gallery=gallery, file_full_name=request.data["file_full_name"]
    )
    file.delete()
    # TODO DELETE FILE CONCERNED
    return Response(FileSerializer(file).data)


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    permission_classes = [IsAdminUser]

    def put(self, request, filename, format="jpg"):
        file_obj = request.data["file"]
        file = open(str(settings.BASE_DIR) + "/galerie/media/" + filename)
        for chunk in file_obj.chunks():
            file.write(chunk)
        file.close()
        return Response(status=204)


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdminUser])
def import_users(request):
    read_users(str(settings.BASE_DIR) + "/api/users.sql")
    return Response(status=200)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def years(request):
    years = Year.objects.all().order_by("pk")
    serializer = YearSerializer(years, many=True)
    return Response(serializer.data)

def read_users(file):
    f = open(file, encoding="utf8")
    f.readline()
    i = 0
    for l in f:
        if i < 10:
            args = l.replace("(", "").replace(")", "").split(",")
            uid = int(args[0])
            firstname = args[2].replace("'", "").replace(" ", "")
            lastname = args[3].replace("'", "").replace(" ", "")
            year = args[6].replace("'", "")
            username = args[8].replace("'", "").replace(" ", "").lower()
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
