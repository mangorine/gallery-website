from api.models import File, Gallery, Promo, Student, Year
from django.contrib.auth import models
from django.test import TestCase


class YearModelTest(TestCase):
    def test_year_saves_in_database(self):
        year = Year(name="Promododo")
        year.save()
        retrieved_year = Year.objects.get(pk=year.pk)
        self.assertEqual(retrieved_year.pk, year.pk)


class PromoModelTest(TestCase):
    def test_promo_saves_in_database(self):
        year = Year(name="Promododo")
        year.save()
        promo = Promo(name="Promododo", first_year=year)
        promo.save()
        retrieved_promo = Promo.objects.get(pk=promo.pk)
        self.assertEqual(retrieved_promo.pk, promo.pk)
