from django.urls import path
from gestion.views import gallery_view, index_view

urlpatterns = [path("", index_view), path("gallery/<slug:slug>", gallery_view)]
