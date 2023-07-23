from django.urls import path

from restaurant_app.views import (
    Index,
    DishListView,
    CookListView,
    DishTypeListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    DishCreateView,
    DishDetailView,
    DishUpdateView,
    DishDeleteView,
    CookDeleteView,
    DishTypeCreateView,
    DishTypeDetailView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path(
        "dish_types/<int:pk>/update",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish_types/<int:pk>/delete",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/create", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete", CookDeleteView.as_view(), name="cook-delete"),
]
