from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.showEntry, name="title"),
    path("random", views.randomEntry, name="random"),
    path("newentry", views.newEntry, name="newentry"),
    path("edit/<str:title>", views.editEntry, name="editentry"),
]
