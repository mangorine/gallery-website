from django.urls import path
from api.views import(
    getRoutes,
    get_galleries,
    get_pics
)

urlpatterns = [
    path("", getRoutes),
    path("galleries/", get_galleries), 
    path("gallery/pics/", get_pics)
]
