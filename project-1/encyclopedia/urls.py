from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.showEntry, name="title"),
    path("edit/<str:title>", views.editEntry, name="editentry"),
    path("random", views.randomEntry, name="random"),
    path("newentry", views.newEntry, name="newentry"),
    path("search", views.search, name="search"),

]
