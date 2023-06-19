from rest_framework import serializers
from api.models import (
    Student, Gallery, Material, File, Reaction
)
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'id']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = ['id', 'user', 'promotion']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'name', 'description', 'date', 'visibility', 'type']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file_name', 'file_extension', 'file_full_name', 'gallery', 'link']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name']

class ReactionSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    gallery = GallerySerializer()
    class Meta:
        model = Reaction
        fields = ['gallery', 'student']
