from django.urls import path

from restaurant_app.views import Index, DishListView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list")
]
