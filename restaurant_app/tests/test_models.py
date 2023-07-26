from django.test import TestCase
from restaurant_app.models import DishType, Cook, Dish


class DishTypeModelTest(TestCase):
    def test_str_method(self):
        dish_type = DishType.objects.create(name="Main Course")
        self.assertEqual(str(dish_type), "Main Course")


class CookModelTest(TestCase):
    def test_str_method(self):
        cook = Cook.objects.create(username="chef_john", years_of_experience=10)
        self.assertEqual(str(cook), "chef_john")


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.cook = Cook.objects.create(username="chef_john", years_of_experience=10)

    def test_str_method(self):
        dish = Dish.objects.create(
            name="Pasta",
            description="Delicious pasta dish",
            price=12.99,
            dish_type=self.dish_type,
        )
        self.assertEqual(str(dish), "Pasta")

    def test_cook_association(self):
        dish = Dish.objects.create(
            name="Pasta",
            description="Delicious pasta dish",
            price=12.99,
            dish_type=self.dish_type,
        )
        dish.cooks.add(self.cook)
        self.assertIn(self.cook, dish.cooks.all())

    def test_dish_type_association(self):
        dish = Dish.objects.create(
            name="Pasta",
            description="Delicious pasta dish",
            price=12.99,
            dish_type=self.dish_type,
        )
        self.assertEqual(dish.dish_type, self.dish_type)


class ModelTestCase(TestCase):
    def test_dish_type_model(self):
        dish_type = DishType.objects.create(name="Test Dish Type")
        self.assertEqual(str(dish_type), "Test Dish Type")

    def test_cook_model(self):
        cook = Cook.objects.create(username="test_cook", years_of_experience=5)
        self.assertEqual(str(cook), "test_cook")

    def test_dish_model(self):
        dish_type = DishType.objects.create(name="Test Dish Type")
        cook = Cook.objects.create(username="test_cook", years_of_experience=5)
        dish = Dish.objects.create(
            name="Test Dish",
            description="Test description",
            price=9.99,
            dish_type=dish_type,
        )
        dish.cooks.add(cook)

        self.assertEqual(str(dish), "Test Dish")
        self.assertIn(cook, dish.cooks.all())
        self.assertEqual(dish.dish_type, dish_type)
