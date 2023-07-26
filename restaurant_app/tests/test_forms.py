from django.test import TestCase
from restaurant_app.models import Cook, Dish, DishType
from restaurant_app.forms import (
    DishTypeForm,
    DishForm,
    CookUpdateForm,
    UserLoginForm,
    RegistrationForm,
)


class FormsTestCase(TestCase):
    def test_dish_type_form_valid_data(self):
        form = DishTypeForm(data={"name": "Dessert"})
        self.assertTrue(form.is_valid())

    def test_dish_type_form_invalid_data(self):
        form = DishTypeForm(data={})  # Empty data, should be invalid
        self.assertFalse(form.is_valid())

    def test_dish_form_valid_data(self):
        form = DishForm(data={"name": "Pasta", "cooks": [self.create_cook()]})
        self.assertTrue(form.is_valid())

    def test_dish_form_invalid_data(self):
        form = DishForm(data={})  # Empty data, should be invalid
        self.assertFalse(form.is_valid())

    def test_cook_update_form_valid_data(self):
        form = CookUpdateForm(data={"years_of_experience": 5})
        self.assertTrue(form.is_valid())

    def test_cook_update_form_invalid_data(self):
        form = CookUpdateForm(
            data={"years_of_experience": -1}
        )  # Negative value, should be invalid
        self.assertFalse(form.is_valid())

    def test_user_login_form_valid_data(self):
        form = UserLoginForm(data={"username": "testuser", "password": "testpassword"})
        self.assertTrue(form.is_valid())

    def test_user_login_form_invalid_data(self):
        form = UserLoginForm(
            data={"username": "", "password": ""}
        )  # Empty data, should be invalid
        self.assertFalse(form.is_valid())

    def test_registration_form_valid_data(self):
        form = RegistrationForm(
            data={
                "username": "newuser",
                "email": "newuser@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "years_of_experience": 3,
                "password1": "testpassword",
                "password2": "testpassword",
            }
        )
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid_data(self):
        form = RegistrationForm(
            data={
                "username": "",
                "email": "invalid_email",
                "first_name": "",
                "last_name": "",
                "years_of_experience": -1,  # Negative value, should be invalid
                "password1": "testpassword",
                "password2": "differentpassword",  # Non-matching passwords, should be invalid
            }
        )
        self.assertFalse(form.is_valid())
