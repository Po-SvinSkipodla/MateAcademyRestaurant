from django.test import TestCase

from restaurant_app.forms import CookCreationForm


class CookCreationTest(TestCase):
    def test_years_of_experience_validation(self):
        form_data = {
            "username": "Bob",
            "password": "123123aasds",
            "years_of_experience": -4,
        }

        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
