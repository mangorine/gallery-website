from django.contrib import admin

from api.models import File, Gallery, Student, Year, Promo

# Register your models here.
admin.site.register(Year)
admin.site.register(Promo)
admin.site.register(Student)
admin.site.register(Gallery)
admin.site.register(File)
