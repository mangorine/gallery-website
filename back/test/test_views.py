from api.views import getRoutes
from django.contrib.auth.views import LoginView
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from galerie.views import galleries, gallery, index, material
from gestion.views import index_view


class TestUrls(SimpleTestCase):
    def test_login_url_resolves(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_index_url_resolves(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func, index)

    def test_gallery_url_resolves(self):
        url = reverse("gallery", args=["slug"])
        self.assertEquals(resolve(url).func, gallery)

    def test_galleries_url_resolves(self):
        url = reverse("galleries")
        self.assertEquals(resolve(url).func, galleries)

    def test_material_url_resolves(self):
        url = reverse("material")
        self.assertEquals(resolve(url).func, material)

    def test_gestion_url_resolves(self):
        url = reverse("gestion")
        self.assertEquals(resolve(url).func, index_view)

    def test_api_url_resolves(self):
        url = reverse("api-routes")
        self.assertEquals(resolve(url).func, getRoutes)
