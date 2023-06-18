from django.contrib import admin

from api.models import (
    File, Gallery, Material, Reaction, Student
)

# Register your models here.

admin.site.register(Student)
admin.site.register(Gallery)
admin.site.register(File)