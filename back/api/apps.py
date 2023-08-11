from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        from api.models import Promo, Student
        from django.contrib.auth.models import User
        from django_cas_ng.signals import cas_user_authenticated

        @receiver(cas_user_authenticated)
        def user_auth(sender, **kwargs):
            args = {}
            args.update(kwargs)
            print(args.get("user"))

        @receiver(post_save, sender=User)
        def user_saved(sender, instance, created, **kwargs):
            print("user saved")
            if created:
                student = Student(user=instance, promo=Promo.objects.last())
                student.save()
