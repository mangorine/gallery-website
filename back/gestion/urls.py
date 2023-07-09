from django.urls import path
from gestion.views import(
    index_view,
    gallery_view
)

urlpatterns = [
    path('', index_view),
    path('gallery/<int:id>', gallery_view)
]    

