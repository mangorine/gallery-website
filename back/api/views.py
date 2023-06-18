from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from api.models import (
    Student, Gallery, File, Reaction, Material
)

from api.serializers import (
    GallerySerializer, FileSerializer
)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/api/galleries",
            "method": "GET",
            "description": "Return all galleries that a user can see",
        },
        {
            "Endpoint": "/api/gallery/pics",
            "method": "GET",
            "description": "Return all pics from a gallery",
            "Format of the request:": {
                "id": "gallery_id",
            },
        }
    ]

    return Response(routes)

@login_required
@api_view(['GET'])
def get_galleries(request):
    galleries = Gallery.objects.all()
    serializer = GallerySerializer(galleries, many=True)
    return Response(serializer.data)

@login_required
@api_view(['POST'])
def get_pics(request):
    files = File.objects.filter(gallery = request.data['id'])
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)
