from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("name", views.returnName, name="returnName"),
    path("cat", views.returnCat, name="returnCat"),
    path("dog", views.returnDog, name="returnDog"),
    path("<str:greet_name>", views.greet, name="greet"),
]