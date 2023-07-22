from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant_app.models import Cook, Dish, DishType


class Index(generic.TemplateView):
    template_name = "restaurant_app/index.html"


class DishListView(generic.ListView):
    model = Dish


class CookListView(generic.ListView):
    model = Cook


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "restaurant_app/dish_type_list.html"


# class CookCreateView(generic.CreateView):
#     model = Cook
#     form_class = CookCreationForm
#     success_url = reverse_lazy("restaurant:")

