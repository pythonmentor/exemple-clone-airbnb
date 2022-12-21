from django.urls import path

from .views import home, search, book, success


urlpatterns = [
    path("", home, name="home"),
    path("search/", search, name="search"),
    path("book", book, name="book"),
    path("success", success, name="success"),
]
