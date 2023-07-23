from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant_app.forms import CookCreationForm, CookLicenseUpdateForm
from restaurant_app.models import Cook, Dish, DishType


class Index(generic.TemplateView):
    template_name = "restaurant_app/index.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookLicenseUpdateForm
    success_url = reverse_lazy("cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook


class CookDetailView(generic.DetailView):
    model = Cook


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "restaurant_app/dish_type_list.html"


# class CookCreateView(generic.CreateView):
#     model = Cook
#     form_class = CookCreationForm
#     success_url = reverse_lazy("restaurant:")
