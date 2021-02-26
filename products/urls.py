from django.urls import path
from .views import CategoryView, DrinkView

urlpatterns = [
    path('/categories', CategoryView.as_view()),
    path('/drinks', DrinkView.as_view())
]
