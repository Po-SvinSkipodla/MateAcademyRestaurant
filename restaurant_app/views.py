from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant_app.forms import (
    # CookCreationForm,
    DishForm,
    CookUpdateForm,
    DishTypeForm,
    UserLoginForm,
    RegistrationForm,
    CookSearchForm,
    SearchForm,
)
from restaurant_app.models import Cook, Dish, DishType


class Index(generic.TemplateView):
    template_name = "restaurant_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_cooks"] = Cook.objects.count()
        context["num_dishes"] = Dish.objects.count()
        context["num_dish_types"] = DishType.objects.count()
        return context


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name:
                queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_form"] = SearchForm()

        return context


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("dish-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("cook-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if username:
                queryset = queryset.filter(username__icontains=username)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_form"] = CookSearchForm()

        return context


class CookDetailView(generic.DetailView):
    model = Cook


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "restaurant_app/dish_type_list.html"
    context_object_name = "dish_types_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            if name:
                queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_form"] = SearchForm()

        return context


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "restaurant_app/dish_type_detail.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "restaurant_app/dish_type_form.html"
    success_url = reverse_lazy("dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "restaurant_app/dish_type_form.html"
    success_url = reverse_lazy("dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "restaurant_app/dish_type_confirm_delete.html"
    success_url = reverse_lazy("dish-type-list")


class UserLoginView(LoginView):
    template_name = "accounts/sign-in.html"
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy("index")


class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "accounts/sign-up.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        print("Account created successfully!")
        return response

    def form_invalid(self, form):
        print("Registration failed!")
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy("index")
