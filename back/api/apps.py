from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
import galerie.settings as settings

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from api.models import(
            Student, Promo
        )
        from django.contrib.auth.models import User

        @receiver(post_save, sender=User)
        def user_saved(sender, instance, created, **kwargs):
            if created:
                student = Student(user = instance, promo = Promo.objects.last())
                student.save()

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
        
        #read_users(str(settings.BASE_DIR) + '/api/users.sql')

