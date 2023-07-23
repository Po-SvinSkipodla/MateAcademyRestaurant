from django.urls import path

from restaurant_app.views import (
    Index,
    DishListView,
    CookListView,
    DishTypeListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/create", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
]
