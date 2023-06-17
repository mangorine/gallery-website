from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path("accounts/", include("django.contrib.auth.urls")),

]
